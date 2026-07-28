# app/core/config/manager.py
from pathlib import Path
from typing import Any

from app.core.config.loader import ConfigLoader
from app.core.config.validator import (
    ConfigValidator,
)


class ConfigManager:
    """
    Central configuration manager.

    Responsible for:
    - Loading YAML configs
    - Validating configs
    - Providing access to services
    """


    def __init__(
        self,
        config_directory: Path
    ):

        self.config_directory = (
            config_directory
        )

        self.loader = ConfigLoader(
            config_directory
        )

        self.validator = ConfigValidator()

        self.config: dict[str, Any] = {}



    def load(
        self
    ) -> None:

        self.config = (
            self.loader.load_yaml()
        )



    def validate(
        self
    ) -> None:

        required = [
            "redis",
            "worker",
        ]

        self.validator.validate_required_keys(
            self.config,
            required
        )



    def initialize(
        self
    ) -> None:

        self.load()

        self.validate()



    def get(
        self,
        key: str,
        default=None
    ):

        return self.config.get(
            key,
            default
        )