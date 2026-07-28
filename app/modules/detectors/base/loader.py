# app/modules/detectors/base/loader.py
from __future__ import annotations
from typing import Type
from app.modules.detectors.base.detector import BaseDetector

class DetectorLoader:
    """
    Registry responsible for storing and creating detectors.
    """

    def __init__(self):
        self._registry: dict[str, Type[BaseDetector]] = {}

    def register(
        self,
        name: str,
        detector: Type[BaseDetector],
    ) -> None:
        """
        Register a detector class.
        """
        self._registry[name.lower()] = detector

    def create(
        self,
        name: str,
    ) -> BaseDetector:
        """
        Create a detector instance.
        """
        detector = self._registry.get(name.lower())
        if detector is None:
            raise ValueError(
                f"Detector '{name}' is not registered."
            )

        return detector()

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check if detector exists.
        """
        return name.lower() in self._registry

    def registered(self) -> list[str]:
        """
        Return all registered detectors.
        """
        return sorted(self._registry.keys())