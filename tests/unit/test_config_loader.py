from pathlib import Path

from app.core.config.loader import ConfigLoader


def test_yaml_loader():

    config_file = Path(
        "app/core/config/test.yaml"
    )

    loader = ConfigLoader(
        config_file
    )

    config = loader.load_yaml()

    print(config)

    assert config["redis"]["host"] == "localhost"
    assert config["redis"]["port"] == 6379
    assert config["worker"]["count"] == 5