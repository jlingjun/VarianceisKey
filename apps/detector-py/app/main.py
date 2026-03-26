from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Local AI Text Detector",
    description="Local-first AI text detection service",
    version="1.0.0",
)

app.include_router(router)


@app.on_event("startup")
async def startup_event():
    from app.model.loader import model_loader
    model_loader.load()
