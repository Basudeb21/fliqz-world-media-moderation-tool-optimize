# app/core/redis/client.py
"""
Redis Client
Low-level Redis connection manager.
This module ONLY manages Redis connections.
Do not put any business logic here.
"""

from __future__ import annotations
from typing import Optional
import redis
from app.core.config.settings import settings
from app.core.logger import get_logger

logger = get_logger("RedisClient")
class RedisClient:
    """
    Singleton Redis connection manager.
    """
    _pool: Optional[redis.ConnectionPool] = None
    _client: Optional[redis.Redis] = None

    @classmethod
    def get_client(cls) -> redis.Redis:
        """
        Returns a singleton Redis client.
        """
        if cls._client is None:
            logger.info("Initializing Redis connection...")
            cls._pool = redis.ConnectionPool(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB,
                password=settings.REDIS_PASSWORD,
                decode_responses=True,
                max_connections=100,
                health_check_interval=30,
            )

            cls._client = redis.Redis(
                connection_pool=cls._pool
            )
            cls._client.ping()
            logger.info("Redis connected successfully.")
        return cls._client

    @classmethod
    def is_alive(cls) -> bool:
        """
        Returns True if Redis is reachable.
        """
        try:
            return cls.get_client().ping()
        except redis.RedisError as exc:
            logger.exception(f"Redis unavailable: {exc}")
            return False

    @classmethod
    def close(cls) -> None:
        """
        Close Redis client.
        """
        if cls._client is not None:
            cls._client.close()
            cls._client = None
            cls._pool = None
            logger.info("Redis connection closed.")