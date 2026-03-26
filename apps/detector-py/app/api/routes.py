from fastapi import APIRouter, HTTPException
from app.schemas.request import DetectRequest
from app.schemas.response import DetectResponse, HealthResponse
from app.core.detector import TextDetector

router = APIRouter()
detector = TextDetector()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="ok")


@router.post("/detect", response_model=DetectResponse)
async def detect_text(request: DetectRequest):
    if not request.text or not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    try:
        result = detector.detect(request.text)
        return DetectResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
