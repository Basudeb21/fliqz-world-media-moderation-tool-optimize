# app/core/metrics/registry.py
from prometheus_client import CollectorRegistry

class MetricsRegistry:
    """
    Central Prometheus registry.
    Every service uses the same registry
    to expose metrics.
    """


    def __init__(self):
        self.registry = CollectorRegistry()

    def get_registry(
        self
    ) -> CollectorRegistry:
        """
        Return Prometheus registry.
        """
        return self.registry


# Singleton registry instance
metrics_registry = MetricsRegistry()