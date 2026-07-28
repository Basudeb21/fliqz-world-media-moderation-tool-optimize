# app/modules/detectors/base/schemas.py
from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

from app.common.media.asset import MediaAsset


# ==========================================================
# Media Types
# ==========================================================

class MediaType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"


# ==========================================================
# Detector Status
# ==========================================================

class DetectorStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"


# ==========================================================
# Detector Types
# ==========================================================

class DetectorType(str, Enum):
    WEAPON = "weapon"
    NSFW = "nsfw"
    MINOR = "minor"
    FACE = "face"
    ALCOHOL = "alcohol"
    SMOKING = "smoking"
    DRUGS = "drugs"
    VIOLENCE = "violence"
    ANIMAL = "animal"
    LOGO = "logo"
    SELF_HARM = "self_harm"
    PII = "pii"
    CUSTOM = "custom"


# ==========================================================
# Bounding Box
# ==========================================================

class BoundingBox(BaseModel):
    x1: float
    y1: float
    x2: float
    y2: float


# ==========================================================
# Single Detection
# ==========================================================

class Detection(BaseModel):
    label: str

    confidence: float = Field(
        ge=0.0,
        le=1.0,
    )

    bbox: BoundingBox | None = None

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )


# ==========================================================
# Detector Configuration
# ==========================================================

class DetectorConfig(BaseModel):
    enabled: bool = True

    confidence_threshold: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
    )

    device: str = "auto"

    model_path: str | None = None

    extra: dict[str, Any] = Field(
        default_factory=dict
    )


# ==========================================================
# Detection Request
# ==========================================================

class DetectionRequest(BaseModel):
    """
    Input passed to every detector.
    """

    media: MediaAsset

    config: DetectorConfig | None = None

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )

    model_config = {
        "arbitrary_types_allowed": True,
    }


# ==========================================================
# Detection Result
# ==========================================================

class DetectionResult(BaseModel):
    detector: DetectorType

    status: DetectorStatus

    detections: list[Detection] = Field(
        default_factory=list
    )

    processing_time_ms: float = 0.0

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )

    error: str | None = None

    @property
    def detected(self) -> bool:
        return bool(self.detections)

    @property
    def max_confidence(self) -> float:
        if not self.detections:
            return 0.0

        return max(
            detection.confidence
            for detection in self.detections
        )   