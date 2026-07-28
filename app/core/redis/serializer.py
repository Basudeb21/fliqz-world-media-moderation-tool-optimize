# app/core/redis/serializer.py
"""
Redis Serializer
Centralized JSON serialization/deserialization for Redis.

Never call json.dumps() or json.loads()
outside this module.
"""

from __future__ import annotations
import json
from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

class RedisSerializer:
    """
    Serialize Python objects for Redis storage.
    """
    @staticmethod
    def _default(obj):
        """
        Handles non-JSON-native objects.
        """
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, Decimal):
            return float(obj)
        if hasattr(obj, "model_dump"):
            return obj.model_dump()
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        raise TypeError(
            f"Object of type {type(obj).__name__} "
            "is not JSON serializable."
        )

    @classmethod
    def dumps(cls, value) -> str:
        """
        Serialize Python object to JSON string.
        """
        return json.dumps(
            value,
            default=cls._default,
            ensure_ascii=False,
            separators=(",", ":"),
        )

    @staticmethod
    def loads(value: str):
        """
        Deserialize JSON string to Python object.
        """
        if value is None:
            return None
        return json.loads(value)