# app/common/media/loader.py
from __future__ import annotations

import mimetypes
from pathlib import Path

import cv2

from app.common.media.asset import MediaAsset
from app.modules.detectors.base.schemas import MediaType


class MediaLoader:
    """
    Loads media from disk into a MediaAsset.
    """

    IMAGE_EXTENSIONS = {
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp",
        ".webp",
        ".gif",
    }

    VIDEO_EXTENSIONS = {
        ".mp4",
        ".mov",
        ".avi",
        ".mkv",
        ".webm",
        ".mpeg",
    }

    @classmethod
    def load(
        cls,
        path: str | Path,
    ) -> MediaAsset:

        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(path)

        suffix = path.suffix.lower()

        if suffix in cls.IMAGE_EXTENSIONS:
            return cls._load_image(path)

        if suffix in cls.VIDEO_EXTENSIONS:
            return cls._load_video(path)

        raise ValueError(
            f"Unsupported media type: {suffix}"
        )

    @classmethod
    def _load_image(
        cls,
        path: Path,
    ) -> MediaAsset:

        image = cv2.imread(str(path))

        if image is None:
            raise ValueError(
                f"Unable to load image: {path}"
            )

        height, width = image.shape[:2]

        channels = (
            image.shape[2]
            if len(image.shape) == 3
            else 1
        )

        mime_type = (
            mimetypes.guess_type(path)[0]
            or "application/octet-stream"
        )

        return MediaAsset(
            path=path,
            media_type=MediaType.IMAGE,
            mime_type=mime_type,
            width=width,
            height=height,
            channels=channels,
            size_bytes=path.stat().st_size,
            image=image,
        )

    @classmethod
    def _load_video(
        cls,
        path: Path,
    ) -> MediaAsset:

        capture = cv2.VideoCapture(str(path))

        if not capture.isOpened():
            raise ValueError(
                f"Unable to open video: {path}"
            )

        width = int(
            capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        )

        height = int(
            capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        )

        fps = float(
            capture.get(cv2.CAP_PROP_FPS)
        )

        total_frames = int(
            capture.get(cv2.CAP_PROP_FRAME_COUNT)
        )

        duration = (
            total_frames / fps
            if fps > 0
            else 0.0
        )

        mime_type = (
            mimetypes.guess_type(path)[0]
            or "application/octet-stream"
        )

        return MediaAsset(
            path=path,
            media_type=MediaType.VIDEO,
            mime_type=mime_type,
            width=width,
            height=height,
            fps=fps,
            duration=duration,
            total_frames=total_frames,
            size_bytes=path.stat().st_size,
            video=capture,
        )