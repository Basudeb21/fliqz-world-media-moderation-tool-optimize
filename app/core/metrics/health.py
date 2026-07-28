# app/core/metrics/health.py
from prometheus_client import Gauge

from app.core.metrics.registry import (
    metrics_registry,
)
registry = metrics_registry.get_registry()


# Service Health
SERVICE_HEALTH = Gauge(
    "fliqz_service_health",
    """
    Service health status.
    1 = healthy
    0 = unhealthy
    """,
    [
        "service",
    ],
    registry=registry,
)


# Dependency Health
DEPENDENCY_HEALTH = Gauge(
    "fliqz_dependency_health",
    """
    External dependency status.
    Examples:
    redis
    mysql
    gpu
    """,
    [
        "dependency",
    ],
    registry=registry,
)

def mark_service_healthy(
    service_name: str
):
    """
    Mark service as healthy.
    """

    SERVICE_HEALTH.labels(
        service=service_name
    ).set(1)



def mark_service_unhealthy(
    service_name: str
):
    """
    Mark service as unhealthy.
    """

    SERVICE_HEALTH.labels(
        service=service_name
    ).set(0)



def mark_dependency_status(
    dependency: str,
    healthy: bool
):
    """
    Update dependency health.

    Example:

    Redis connected:
        mark_dependency_status(
            "redis",
            True
        )
    """

    DEPENDENCY_HEALTH.labels(
        dependency=dependency
    ).set(
        1 if healthy else 0
    )