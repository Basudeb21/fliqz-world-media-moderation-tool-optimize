# app/core/redis/service.py
"""
Redis Service
High-level Redis API for the moderation engine.
Every component should use this service instead of interacting
with redis.Redis directly.
Responsibilities:
- JSON serialization
- Basic Redis operations
- Logging
- Error handling

Never import redis.Redis outside app.core.redis.
"""

from __future__ import annotations
from typing import Any
import redis
from app.core.logger import get_logger
from app.core.redis.client import RedisClient
from app.core.redis.serializer import RedisSerializer

logger = get_logger("RedisService")

class RedisService:
    """
    High-level Redis wrapper.
    """

    def __init__(self):

        self._redis = RedisClient.get_client()

    # --------------------------------------------------
    # String Operations
    # --------------------------------------------------

    def set_value(
        self,
        key: str,
        value: str,
        expire: int | None = None,
    ) -> bool:
        """
        Store plain string.
        """

        try:

            return self._redis.set(
                key,
                value,
                ex=expire,
            )

        except redis.RedisError:

            logger.exception(
                f"Failed SET '{key}'"
            )

            raise

    def get_value(
        self,
        key: str,
    ) -> str | None:
        """
        Read plain string.
        """

        try:

            return self._redis.get(key)

        except redis.RedisError:

            logger.exception(
                f"Failed GET '{key}'"
            )

            raise

    # --------------------------------------------------
    # JSON
    # --------------------------------------------------

    def set_json(
        self,
        key: str,
        value: Any,
        expire: int | None = None,
    ) -> bool:
        """
        Store JSON object.
        """

        return self.set_value(
            key=key,
            value=RedisSerializer.dumps(value),
            expire=expire,
        )

    def get_json(
        self,
        key: str,
    ) -> Any:
        """
        Read JSON object.
        """

        value = self.get_value(key)

        return RedisSerializer.loads(value)

    # --------------------------------------------------
    # Generic
    # --------------------------------------------------

    def exists(
        self,
        key: str,
    ) -> bool:

        return bool(
            self._redis.exists(key)
        )

    def delete(
        self,
        *keys: str,
    ) -> int:

        return self._redis.delete(*keys)

    def expire(
        self,
        key: str,
        seconds: int,
    ) -> bool:

        return self._redis.expire(
            key,
            seconds,
        )

    def increment(
        self,
        key: str,
        amount: int = 1,
    ) -> int:

        return self._redis.incr(
            key,
            amount,
        )

    def ping(self) -> bool:

        return self._redis.ping()