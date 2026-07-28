from app.core.metrics import (
    FRAMES_PROCESSED_TOTAL,
    DETECTION_RESULTS_TOTAL,
    QUEUE_SIZE,
    mark_service_healthy,
)


def test_metrics():

    FRAMES_PROCESSED_TOTAL.inc()


    DETECTION_RESULTS_TOTAL.labels(
        detector="minor",
        result="blocked"
    ).inc()


    QUEUE_SIZE.labels(
        queue_name="minor_queue"
    ).set(100)


    mark_service_healthy(
        "test_worker"
    )