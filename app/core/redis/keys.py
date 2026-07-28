# app/core/redis/keys.py
"""
Redis Key Schema
This module is the SINGLE SOURCE OF TRUTH for every Redis key
used by the FliqzWorld AI Moderation Engine.
Never concatenate Redis keys manually anywhere else.

Example:
    RedisKeys.attachment(101)

instead of
    f"attachment:{attachment_id}"
"""

from __future__ import annotations

class RedisKeys:
    """
    Redis key factory.
    Key namespace:
        fm = Fliqz Moderation
    """
    PREFIX = "fm"

    # Queue Keys
    @classmethod
    def queue(
        cls,
        name: str,
    ) -> str:
        """
        Example:
            fm:queue:minor
            fm:queue:nsfw
        """

        return f"{cls.PREFIX}:queue:{name}"

    # Attachment
    @classmethod
    def attachment(
        cls,
        attachment_id: int,
    ) -> str:
        """
        Example:
            fm:attachment:101
        """

        return (
            f"{cls.PREFIX}:attachment:{attachment_id}"
        )

    @classmethod
    def progress(
        cls,
        attachment_id: int,
    ) -> str:
        """
        Example:

            fm:attachment:101:progress
        """

        return (
            f"{cls.attachment(attachment_id)}:progress"
        )

    @classmethod
    def cancellation(
        cls,
        attachment_id: int,
    ) -> str:
        """
        Example:

            fm:attachment:101:cancel
        """

        return (
            f"{cls.attachment(attachment_id)}:cancel"
        )

    # Chunk
    @classmethod
    def chunk(
        cls,
        attachment_id: int,
        chunk_id: int,
    ) -> str:
        """
        Example:

            fm:attachment:101:chunk:7
        """

        return (
            f"{cls.attachment(attachment_id)}"
            f":chunk:{chunk_id}"
        )

    # Detector
    @classmethod
    def detector_result(
        cls,
        attachment_id: int,
        detector: str,
    ) -> str:
        """
        Example:

            fm:attachment:101:detector:minor
        """

        return (
            f"{cls.attachment(attachment_id)}"
            f":detector:{detector}"
        )

    # Worker
    @classmethod
    def worker(
        cls,
        worker_type: str,
        worker_id: str,
    ) -> str:
        """
        Example:

            fm:worker:minor:001
        """

        return (
            f"{cls.PREFIX}:worker:"
            f"{worker_type}:{worker_id}"
        )

    @classmethod
    def heartbeat(
        cls,
       worker_type: str,
        worker_id: str,
    ) -> str:
        """
        Example:
            fm:heartbeat:minor:001
        """

        return (
            f"{cls.PREFIX}:heartbeat:"
            f"{worker_type}:{worker_id}"
        )

    # Locks
    @classmethod
    def lock(
        cls,
        resource: str,
    ) -> str:
        """
        Example:

            fm:lock:attachment:101
        """

        return (
            f"{cls.PREFIX}:lock:{resource}"
        )

    # Retry
    @classmethod
    def retry(
        cls,
        job_id: str,
    ) -> str:
        """
        Retry information for a job.
        """

        return (
            f"{cls.PREFIX}:retry:{job_id}"
        )

    @classmethod
    def dead_letter(
        cls,
        queue_name: str,
    ) -> str:
        """
        Dead letter queue.

        Example:

            fm:deadletter:minor
        """

        return (
            f"{cls.PREFIX}:deadletter:{queue_name}"
        )