# app/common/media/frames.py
from __future__ import annotations
from typing import Generator
import cv2
import numpy as np
from app.common.media.asset import MediaAsset

class FrameExtractor:
    """
    Extracts frames from a video.
    """
    @staticmethod
    def iterate(
        media: MediaAsset,
        sample_rate: int = 1,
    ) -> Generator[np.ndarray, None, None]:

        if media.video is None:
            raise ValueError(
                "MediaAsset does not contain a video."
            )
        capture = media.video
        frame_index = 0
        while True:
            success, frame = capture.read()
            if not success:
                break

            if frame_index % sample_rate == 0:
                yield frame
            frame_index += 1

        capture.set(
            cv2.CAP_PROP_POS_FRAMES,
            0,
        )

    @staticmethod
    def extract(
        media: MediaAsset,
        sample_rate: int = 1,
    ) -> list[np.ndarray]:

        return list(
            FrameExtractor.iterate(
                media,
                sample_rate,
            )
        )