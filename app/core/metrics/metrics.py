# app/core/metrics/metrics.py
from prometheus_client import (
    Counter,
    Gauge,
    Histogram,
)

from app.core.metrics.registry import (
    metrics_registry,
)


registry = metrics_registry.get_registry()



# Processing Metrics
CHUNKS_PROCESSED_TOTAL = Counter(
    "fliqz_chunks_processed_total",
    "Total number of processed video chunks",
    registry=registry,
)


FRAMES_PROCESSED_TOTAL = Counter(
    "fliqz_frames_processed_total",
    "Total number of processed frames",
    registry=registry,
)


FAILED_JOBS_TOTAL = Counter(
    "fliqz_failed_jobs_total",
    "Total number of failed moderation jobs",
    registry=registry,
)


CANCELLED_JOBS_TOTAL = Counter(
    "fliqz_cancelled_jobs_total",
    "Total number of cancelled jobs",
    registry=registry,
)



# Detection Metrics
DETECTION_TIME = Histogram(
    "fliqz_detection_duration_seconds",
    "Time spent running detector inference",
    registry=registry,
)


DETECTION_RESULTS_TOTAL = Counter(
    "fliqz_detection_results_total",
    "Total detector decisions",
    [
        "detector",
        "result",
    ],
    registry=registry,
)



# Worker Metrics
ACTIVE_WORKERS = Gauge(
    "fliqz_active_workers",
    "Number of active workers",
    [
        "worker_type",
    ],
    registry=registry,
)



QUEUE_SIZE = Gauge(
    "fliqz_queue_size",
    "Current queue size",
    [
        "queue_name",
    ],
    registry=registry,
)


# GPU Metrics
GPU_UTILIZATION = Gauge(
    "fliqz_gpu_utilization_percent",
    "GPU utilization percentage",
    [
        "gpu_id",
    ],
    registry=registry,
)


GPU_MEMORY_USAGE = Gauge(
    "fliqz_gpu_memory_usage_bytes",
    "GPU memory usage",
    [
        "gpu_id",
    ],
    registry=registry,
)