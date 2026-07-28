# app/common/media/resize.py
from __future__ import annotations
import cv2
import numpy as np

class ImageResizer:
    """
    Common image preprocessing utilities.
    """
    @staticmethod
    def resize(
        image: np.ndarray,
        width: int,
        height: int,
    ) -> np.ndarray:
        """
        Simple resize.
        """
        return cv2.resize(
            image,
            (width, height),
            interpolation=cv2.INTER_LINEAR,
        )

    @staticmethod
    def keep_aspect_ratio(
        image: np.ndarray,
        max_width: int,
        max_height: int,
    ) -> np.ndarray:
        """
        Resize while preserving aspect ratio.
        """
        h, w = image.shape[:2]
        scale = min(
            max_width / w,
            max_height / h,
        )

        new_w = int(w * scale)
        new_h = int(h * scale)
        return cv2.resize(
            image,
            (new_w, new_h),
            interpolation=cv2.INTER_LINEAR,
        )

    @staticmethod
    def letterbox(
        image: np.ndarray,
        width: int,
        height: int,
        color=(114, 114, 114),
    ) -> np.ndarray:
        """
        Resize with padding.
        Compatible with YOLO.
        """
        h, w = image.shape[:2]
        scale = min(
            width / w,
            height / h,
        )
        nw = int(w * scale)
        nh = int(h * scale)
        resized = cv2.resize(
            image,
            (nw, nh),
            interpolation=cv2.INTER_LINEAR,
        )

        canvas = np.full(
            (height, width, 3),
            color,
            dtype=np.uint8,
        )
        x = (width - nw) // 2
        y = (height - nh) // 2
        canvas[y:y + nh, x:x + nw] = resized
        return canvas

    @staticmethod
    def thumbnail(
        image: np.ndarray,
        size: int = 256,
    ) -> np.ndarray:
        """
        Generate a thumbnail.
        """
        return ImageResizer.keep_aspect_ratio(
            image,
            size,
            size,
        )