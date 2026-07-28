from typing import Any


class ConfigValidationError(Exception):
    """
    Raised when configuration validation fails.
    """
    pass



class ConfigValidator:
    """
    Validates dynamic YAML configuration files.
    """


    def validate_required_keys(
        self,
        config: dict[str, Any],
        required_keys: list[str]
    ) -> None:

        missing = [
            key
            for key in required_keys
            if key not in config
        ]

        if missing:
            raise ConfigValidationError(
                f"Missing required configuration keys: {missing}"
            )



    def validate_threshold(
        self,
        value: float,
        name: str
    ) -> None:

        if not 0 <= value <= 1:
            raise ConfigValidationError(
                f"{name} must be between 0 and 1. "
                f"Received: {value}"
            )



    def validate_detector(
        self,
        detector_name: str,
        detector_config: dict[str, Any]
    ) -> None:


        if "enabled" not in detector_config:
            raise ConfigValidationError(
                f"{detector_name}: missing enabled field"
            )


        if "priority" in detector_config:

            if not isinstance(
                detector_config["priority"],
                int
            ):
                raise ConfigValidationError(
                    f"{detector_name}: priority must be integer"
                )



        if "threshold" in detector_config:

            self.validate_threshold(
                detector_config["threshold"],
                detector_name
            )



    def validate_detectors(
        self,
        detectors: dict[str, Any]
    ) -> None:

        for name, config in detectors.items():

            self.validate_detector(
                name,
                config
            )