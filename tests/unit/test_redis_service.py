# tests/unit/test_redis_service.py
from app.core.redis import RedisService

redis = RedisService()


def test_set_get_value():

    redis.set_value(
        "test:key",
        "hello",
    )

    assert (
        redis.get_value("test:key")
        == "hello"
    )


def test_set_get_json():

    data = {
        "name": "minor",
        "score": 0.98,
    }

    redis.set_json(
        "test:json",
        data,
    )

    assert (
        redis.get_json("test:json")
        == data
    )


def test_exists():

    redis.set_value(
        "exists:key",
        "1",
    )

    assert redis.exists(
        "exists:key"
    )


def test_delete():

    redis.set_value(
        "delete:key",
        "1",
    )

    redis.delete(
        "delete:key"
    )

    assert not redis.exists(
        "delete:key"
    )


def test_increment():

    redis.delete("counter")

    redis.increment("counter")

    redis.increment("counter")

    assert (
        redis.get_value("counter")
        == "2"
    )


def test_ping():

    assert redis.ping()