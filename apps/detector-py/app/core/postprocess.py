import torch
from app.config import settings


def postprocess(score: float, model_name: str) -> dict:
    predicted_class = 0 if score > settings.empirical_threshold else 1
    # confidence_score = score
    
    label_map = {0: "likely_human", 1: "likely_ai"}
    label = label_map.get(predicted_class, "unknown")
    
    return {
        "label": label,
        "score": round(score, 4),
        "model_name": model_name,
    }
