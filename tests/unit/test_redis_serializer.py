from datetime import datetime

from app.core.redis.serializer import RedisSerializer


def test_dict():

    data = {
        "name": "minor",
        "score": 0.98,
    }

    encoded = RedisSerializer.dumps(data)
    decoded = RedisSerializer.loads(encoded)

    assert decoded == data


def test_datetime():

    now = datetime.now()

    encoded = RedisSerializer.dumps(
        {
            "time": now,
        }
    )

    decoded = RedisSerializer.loads(encoded)

    assert decoded["time"] == now.isoformat()


def test_none():

    assert RedisSerializer.loads(None) is None