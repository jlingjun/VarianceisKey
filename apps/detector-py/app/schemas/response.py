from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class DetectResponse(BaseModel):
    label: str
    score: float
    model_name: str
