from app.utils.variater import Variater

def preprocess_text(text: str) -> list[str]:
    if not text or not text.strip():
        return []
    variater=Variater()
    return variater.rewrite_text(text)
    
