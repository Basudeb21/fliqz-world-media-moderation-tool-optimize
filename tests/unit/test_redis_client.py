from app.core.redis.client import RedisClient


def test_singleton():
    client1 = RedisClient.get_client()
    client2 = RedisClient.get_client()
    assert client1 is client2


def test_ping():    
    assert RedisClient.is_alive() is True


def test_close():
    RedisClient.close()
    assert RedisClient._client is None