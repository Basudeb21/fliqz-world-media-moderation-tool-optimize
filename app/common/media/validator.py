# app/common/media/validator.py
from __future__ import annotations
from pathlib import Path
from app.common.media.asset import MediaAsset
from app.modules.detectors.base.schemas import MediaType

class MediaValidator:
    """
    Performs generic validation on media assets.
    """
    DEFAULT_MAX_FILE_SIZE = 500 * 1024 * 1024  # 500 MB
    MIN_IMAGE_WIDTH = 32
    MIN_IMAGE_HEIGHT = 32
    MIN_VIDEO_WIDTH = 32
    MIN_VIDEO_HEIGHT = 32

    @classmethod
    def validate(
        cls,
        media: MediaAsset,
    ) -> None:

        cls.validate_exists(media)
        cls.validate_size(media)

        if media.is_image:
            cls.validate_image(media)

        elif media.is_video:
            cls.validate_video(media)

    @staticmethod
    def validate_exists(
        media: MediaAsset,
    ) -> None:

        if not media.path.exists():
            raise FileNotFoundError(media.path)

    @classmethod
    def validate_size(
        cls,
        media: MediaAsset,
    ) -> None:

        if media.size_bytes > cls.DEFAULT_MAX_FILE_SIZE:
            raise ValueError(
                "Media exceeds maximum allowed size."
            )

    @classmethod
    def validate_image(
        cls,
        media: MediaAsset,
    ) -> None:

        if media.width < cls.MIN_IMAGE_WIDTH:
            raise ValueError(
                "Image width too small."
            )

        if media.height < cls.MIN_IMAGE_HEIGHT:
            raise ValueError(
                "Image height too small."
            )

    @classmethod
    def validate_video(
        cls,
        media: MediaAsset,
    ) -> None:

        if media.width < cls.MIN_VIDEO_WIDTH:
            raise ValueError(
                "Video width too small."
            )

        if media.height < cls.MIN_VIDEO_HEIGHT:
            raise ValueError(
                "Video height too small."
            )

        if media.total_frames <= 0:
            raise ValueError(
                "Video contains no frames."
            )

        if media.fps <= 0:
            raise ValueError(
                "Invalid video FPS."
            )