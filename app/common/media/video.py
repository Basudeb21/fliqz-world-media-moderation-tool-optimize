# app/common/media/video.py
from __future__ import annotations

import cv2
import numpy as np

from app.common.media.asset import MediaAsset


class VideoHelper:
    """
    High-level utilities for working with videos.
    """

    @staticmethod
    def frame_count(media: MediaAsset) -> int:
        if media.video is None:
            raise ValueError("MediaAsset does not contain a video.")

        return media.total_frames

    @staticmethod
    def fps(media: MediaAsset) -> float:
        if media.video is None:
            raise ValueError("MediaAsset does not contain a video.")

        return media.fps

    @staticmethod
    def duration(media: MediaAsset) -> float:
        if media.video is None:
            raise ValueError("MediaAsset does not contain a video.")

        return media.duration

    @staticmethod
    def seek_frame(
        media: MediaAsset,
        frame_number: int,
    ) -> np.ndarray | None:

        if media.video is None:
            raise ValueError("MediaAsset does not contain a video.")

        capture = media.video

        capture.set(
            cv2.CAP_PROP_POS_FRAMES,
            frame_number,
            
        )

        success, frame = capture.read()

        capture.set(
            cv2.CAP_PROP_POS_FRAMES,
            0,
        )

        if not success:
            return None

        return frame

    @staticmethod
    def timestamp_to_frame(
        media: MediaAsset,
        seconds: float,
    ) -> int:

        return int(seconds * media.fps)

    @staticmethod
    def frame_to_timestamp(
        media: MediaAsset,
        frame_number: int,
    ) -> float:

        return frame_number / media.fps