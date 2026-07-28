from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
BASE_DIR = Path(__file__).resolve().parents[3]

class Settings(BaseSettings):
    """
    Global configuration manager for FliqzWorld Moderation Engine.
    Values are loaded from:
    1. Environment variables
    2. .env file
    3. Default values below
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


    # Application

    APP_NAME: str = "FliqzWorld AI Moderation Engine"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # Database - MySQL / MariaDB
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PASSWORD: str = ""
    DB_DATABASE: str = "myvault"

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: Optional[str] = None
    REDIS_BRPOP_TIMEOUT: int = 5

    # Redis Queues
    IMAGE_QUEUE: str = (
        "fliqz_moderation_image_queue"
    )

    VIDEO_QUEUE: str = (
        "fliqz_moderation_video_queue"
    )

    STREAM_QUEUE: str = (
        "fliqz_moderation_stream_queue"
    )

    # LLM / Ollama
    LLAMA_API_URL: str = (
        "http://localhost:11434/api/generate"
    )

    # Storage
    STORAGE_PATH: Path = (
        BASE_DIR / "storage"
    )


    UPLOAD_PATH: Path = (
        STORAGE_PATH / "uploads"
    )


    FRAME_PATH: Path = (
        STORAGE_PATH / "frames"
    )


    EVIDENCE_PATH: Path = (
        STORAGE_PATH / "evidence"
    )


    REPORT_PATH: Path = (
        STORAGE_PATH / "reports"
    )



    # Minor Detector Configuration
    MINOR_AGE_MAX_ESTIMATE: int = 21
    MINOR_VOTE_THRESHOLD: float = 0.70
    MIN_USABLE_FRAMES: int = 5
    MIN_FACE_SIZE: int = 40
    MIN_BLUR_SCORE: float = 15.0
    MINOR_MIN_PERCENT: float = 0.20
    MINOR_MIN_FRAMES: int = 2


    # Detection Defaults
    DEFAULT_CONFIDENCE_THRESHOLD: float = 0.90
    FRAME_SAMPLE_RATE: int = 5
    GPU_ENABLED: bool = True



# Singleton instance
settings = Settings()