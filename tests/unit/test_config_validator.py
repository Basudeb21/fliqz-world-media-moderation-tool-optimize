import pytest

from app.core.config.validator import (
    ConfigValidator,
    ConfigValidationError
)



def test_valid_threshold():

    validator = ConfigValidator()

    validator.validate_threshold(
        0.95,
        "minor"
    )



def test_invalid_threshold():

    validator = ConfigValidator()

    with pytest.raises(
        ConfigValidationError
    ):

        validator.validate_threshold(
            2,
            "minor"
        )