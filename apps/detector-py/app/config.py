from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    detect_model_path: str = Field(
        default="/models/roberta-base-openai-detector",
        description="Path to the detection model"
    )
    detect_device: str = Field(
        default="cuda:0",
        description="Device to run inference on (cpu/cuda:0/cuda:1)"
    )
    detect_max_length: int = Field(
        default=512,
        description="Maximum sequence length for tokenization"
    )
    detect_min_tokens: int = Field(
        default=128,
        description="Minimum number of tokens required for detection"
    )
    gen_llm_base_url: str = Field(
        default="https://api.openai.com/v1",
        description="Base URL for generation LLM"
    )
    gen_llm_api_key: str = Field(
        default="replace_me",
        description="API key for generation LLM"
    )
    gen_llm_model: str = Field(
        default="gpt-3.5-turbo",
        description="Model name for generation LLM"
    )
    empirical_threshold: float = Field(
        default=2.6351518630981445,
        description="Empirical threshold for varybalance score"
    )
    detect_min_tokens: int = Field(
        default=128,
        description="Minimum number of tokens required for detection"
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
