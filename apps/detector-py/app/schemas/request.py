from pydantic import BaseModel, Field


class DetectRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text to analyze")


class DetectResponse(BaseModel):
    label: str = Field(..., description="Detection label (likely_ai or likely_human)")
    score: float = Field(..., description="Varybalance score")
    model_name: str = Field(..., description="Name of the model used")
