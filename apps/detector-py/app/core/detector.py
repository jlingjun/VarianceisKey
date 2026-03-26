import torch
from app.model.loader import model_loader
from app.core.preprocess import preprocess_text
from app.core.postprocess import postprocess
from app.config import settings
from loguru import logger
import transformers
import numpy as np


class TextDetector:
    def __init__(self):
        self.tokenizer = model_loader.tokenizer
        self.model = model_loader.model
        self.model_name = model_loader.model_name
        self.max_length = settings.detect_max_length
        self.ce_loss_fn = torch.nn.CrossEntropyLoss(reduction="none")
        
    def _get_device(self):
        return next(self.model.parameters()).device
    
    @torch.inference_mode()
    def _logits(self, encodings: transformers.BatchEncoding) -> torch.Tensor:
        device = self._get_device()
        enc1 = {k: v.to(device) for k, v in encodings.items()}
        observer_logits = self.model(**enc1).logits
        return observer_logits
    
    def tokenize(self, batch: list[str]) -> transformers.BatchEncoding:
        return self.tokenizer(
            batch,
            return_tensors="pt",
            padding="longest",
            truncation=True,
            max_length=self.max_length,
        )
    
    def logperplexity(self, encoding: transformers.BatchEncoding, logits: torch.Tensor):
        device = self._get_device()
        s_logits = logits[..., :-1, :].contiguous() 
        s_labels = encoding.input_ids[..., 1:].to(device).contiguous() 
        s_attention_mask = encoding.attention_mask[..., 1:].to(device).contiguous() 

        logppl = (self.ce_loss_fn(s_logits.transpose(1, 2), s_labels) * s_attention_mask).sum(1) / s_attention_mask.sum(1)
        logppl = logppl.float().cpu().numpy()
        
        return logppl

    def get_MSD(self, scores):
        total = sum([(scores[i] - scores[0]) ** 2 for i in range(1, len(scores))])
        return total / (len(scores) - 1)
    
    def score_text(self, text: list):
        encodings = self.tokenize(text)
        logits = self._logits(encodings)
        logppl = self.logperplexity(encodings, logits)

        msd = self.get_MSD(logppl.tolist())
        sign = np.sign(logppl[0] - np.average(logppl[1:]))

        varybalance_score = float(np.exp(msd * sign) * logppl[0])
        
        return varybalance_score
    
    def detect(self, text: str) -> dict:
        processed_text = preprocess_text(text)        
        if not processed_text:
            raise ValueError("Text cannot be empty")
        
        token_count = len(self.tokenizer.encode(text))
        if token_count < settings.detect_min_tokens:
            raise ValueError(f"Text too short: minimum {settings.detect_min_tokens} tokens required, got {token_count}")
        
        varybalance_score = self.score_text(processed_text)
        
        result = postprocess(varybalance_score, self.model_name)
        return result
  