from app.core.metrics.registry import (
    metrics_registry,
)

from app.core.metrics.metrics import (
    CHUNKS_PROCESSED_TOTAL,
    FRAMES_PROCESSED_TOTAL,
    FAILED_JOBS_TOTAL,
    CANCELLED_JOBS_TOTAL,
    DETECTION_TIME,
    DETECTION_RESULTS_TOTAL,
    ACTIVE_WORKERS,
    QUEUE_SIZE,
    GPU_UTILIZATION,
    GPU_MEMORY_USAGE,
)

from app.core.metrics.health import (
    SERVICE_HEALTH,
    DEPENDENCY_HEALTH,
    mark_service_healthy,
    mark_service_unhealthy,
    mark_dependency_status,
)


__all__ = [

    # Registry
    "metrics_registry",


    # Processing
    "CHUNKS_PROCESSED_TOTAL",
    "FRAMES_PROCESSED_TOTAL",
    "FAILED_JOBS_TOTAL",
    "CANCELLED_JOBS_TOTAL",


    # Detection
    "DETECTION_TIME",
    "DETECTION_RESULTS_TOTAL",


    # Workers
    "ACTIVE_WORKERS",
    "QUEUE_SIZE",


    # GPU
    "GPU_UTILIZATION",
    "GPU_MEMORY_USAGE",


    # Health
    "SERVICE_HEALTH",
    "DEPENDENCY_HEALTH",
    "mark_service_healthy",
    "mark_service_unhealthy",
    "mark_dependency_status",
]