from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    ARK_API_BASE: str = "https://ark.example.com"
    ARK_API_KEY: str = ""
    ARK_DEFAULT_MODEL: str = "mock-model"
    ARK_KB_ID: str = ""

    TIMEOUT: int = 30
    MAX_RETRIES: int = 3
    RATE_LIMIT_QPS: float = 1.0
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
