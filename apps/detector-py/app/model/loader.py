from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from app.config import settings
from loguru import logger


class ModelLoader:
    _instance = None
    _tokenizer = None
    _model = None
    _model_name = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load(self):
        if self._model is None:
            logger.info(f"Loading model from {settings.detect_model_path}...")
            self._tokenizer = AutoTokenizer.from_pretrained(settings.detect_model_path)
            self._model = AutoModelForCausalLM.from_pretrained(
                settings.detect_model_path,
                torch_dtype=torch.float16,
                device_map="auto",
            )
            self._model.eval()
            self._model_name = settings.detect_model_path.split("/")[-1]
            logger.info(f"Model loaded: {self._model_name}")

    @property
    def tokenizer(self):
        if self._tokenizer is None:
            self.load()
        return self._tokenizer

    @property
    def model(self):
        if self._model is None:
            self.load()
        return self._model

    @property
    def model_name(self):
        if self._model_name is None:
            self.load()
        return self._model_name


model_loader = ModelLoader()
