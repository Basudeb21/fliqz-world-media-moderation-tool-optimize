# app/core/config/loader.py
from pathlib import Path
from typing import Any

import yaml
class ConfigLoader:
    """
    Responsible for loading external configuration files.
    Supported formats:
    - YAML
    Future:
    - JSON
    - TOML
    """

    def __init__(self, config_path: Path):
        self.config_path = config_path

    def load_yaml(self) -> dict[str, Any]:
        """
        Load YAML configuration file.
        Returns:
            dict: Parsed configuration data
        Raises:
            FileNotFoundError:
                If configuration file does not exist.
        """

        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}"
            )


        with self.config_path.open(
            "r",
            encoding="utf-8"
        ) as file:

            data = yaml.safe_load(file)


        return data or {}