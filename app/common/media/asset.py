# app/common/media/asset.py

from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from app.modules.detectors.base.schemas import MediaType

@dataclass(slots=True)
class MediaAsset:
    """
    Represents a loaded media object.
    Shared across every detector.
    """

    path: Path
    media_type: MediaType
    mime_type: str = ""
    width: int = 0
    height: int = 0
    channels: int = 0
    fps: float = 0.0
    duration: float = 0.0
    total_frames: int = 0
    size_bytes: int = 0
    image: Any | None = None
    video: Any | None = None
    frames: list[Any] = field(
        default_factory=list
    )

    thumbnail: Any | None = None
    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    @property
    def resolution(self) -> tuple[int, int]:
        """
        Returns (width, height).
        """
        return self.width, self.height

    @property
    def is_image(self) -> bool:
        return self.media_type == MediaType.IMAGE

    @property
    def is_video(self) -> bool:
        return self.media_type == MediaType.VIDEO

    @property
    def is_stream(self) -> bool:
        return self.media_type == MediaType.STREAM