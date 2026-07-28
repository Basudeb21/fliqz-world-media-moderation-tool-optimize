from app.core.redis.keys import RedisKeys


def test_attachment_key():

    assert (
        RedisKeys.attachment(101)
        == "fm:attachment:101"
    )


def test_chunk_key():

    assert (
        RedisKeys.chunk(101, 7)
        == "fm:attachment:101:chunk:7"
    )


def test_detector_key():

    assert (
        RedisKeys.detector_result(
            101,
            "minor",
        )
        == "fm:attachment:101:detector:minor"
    )


def test_queue_key():

    assert (
        RedisKeys.queue("minor")
        == "fm:queue:minor"
    )


def test_worker_key():

    assert (
        RedisKeys.worker(
            "minor",
            "001",
        )
        == "fm:worker:minor:001"
    )