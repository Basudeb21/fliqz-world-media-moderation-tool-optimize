# tests/unit/test_config_manager.py
from pathlib import Path

from app.core.config.manager import (
    ConfigManager
)


def test_config_manager():

    manager = ConfigManager(
        Path(
            "app/core/config/test.yaml"
        )
    )

    manager.initialize()


    redis = manager.get(
        "redis"
    )


    assert redis["host"] == "localhost"
    assert redis["port"] == 6379