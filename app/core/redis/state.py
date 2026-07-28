# app/core/redis/state.py
"""
Attachment State
High-level attachment state manager.
Workers should NEVER manipulate Redis keys directly.
Example:

    state = AttachmentState(attachment_id=101)
    state.initialize(...)
    state.update_progress(...)
    state.save_detector_result(...)
    state.mark_cancelled()
"""

from __future__ import annotations

from typing import Any

from app.core.redis.keys import RedisKeys
from app.core.redis.service import RedisService


class AttachmentState:

    def __init__(self, attachment_id: int):

        self.attachment_id = attachment_id
        self.redis = RedisService()

    # Root Metadata
    def initialize(
        self,
        metadata: dict[str, Any],
    ) -> bool:
        """
        Create initial attachment metadata.
        """

        return self.redis.set_json(
            RedisKeys.attachment(self.attachment_id),
            metadata,
        )

    def get_metadata(self) -> dict | None:

        return self.redis.get_json(
            RedisKeys.attachment(self.attachment_id)
        )

    # Progress
    def update_progress(
        self,
        progress: dict[str, Any],
    ) -> bool:

        return self.redis.set_json(
            RedisKeys.progress(self.attachment_id),
            progress,
        )

    def get_progress(self):

        return self.redis.get_json(
            RedisKeys.progress(self.attachment_id)
        )

    # Cancellation
    def mark_cancelled(self) -> bool:

        return self.redis.set_value(
            RedisKeys.cancellation(self.attachment_id),
            "1",
        )

    def is_cancelled(self) -> bool:

        return self.redis.exists(
            RedisKeys.cancellation(
                self.attachment_id
            )
        )

    # Detector Results
    def save_detector_result(
        self,
        detector: str,
        result: dict[str, Any],
    ) -> bool:

        return self.redis.set_json(
            RedisKeys.detector_result(
                self.attachment_id,
                detector,
            ),
            result,
        )

    def get_detector_result(
        self,
        detector: str,
    ):

        return self.redis.get_json(
            RedisKeys.detector_result(
                self.attachment_id,
                detector,
            )
        )

    # Cleanup
    def delete(self):

        self.redis.delete(

            RedisKeys.attachment(
                self.attachment_id
            ),

            RedisKeys.progress(
                self.attachment_id
            ),

            RedisKeys.cancellation(
                self.attachment_id
            ),
        )