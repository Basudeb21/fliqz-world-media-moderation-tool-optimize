# app/modules/detectors/base/evidence.py
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any

from app.modules.detectors.base.schemas import BoundingBox
class EvidenceType(str, Enum):
    """
    Supported evidence types.
    """
    IMAGE = "image"
    FRAME = "frame"
    CROP = "crop"
    VIDEO = "video"
    TEXT = "text"
    JSON = "json"


@dataclass(slots=True)
class Evidence:
    """
    Universal evidence produced by detectors.
    """
    detector: str
    evidence_type: EvidenceType
    path: Path | None = None
    bounding_box: BoundingBox | None = None
    confidence: float = 0.0
    label: str = ""
    metadata: dict[str, Any] = field(
        default_factory=dict
    )