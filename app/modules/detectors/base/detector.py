# app/modules/detectors/base/detector.py
from __future__ import annotations

from abc import ABC, abstractmethod
from time import perf_counter

from app.modules.detectors.base.result import ResultBuilder
from app.modules.detectors.base.schemas import (
    DetectionRequest,
    DetectionResult,
    DetectorType,
)


class BaseDetector(ABC):
    """
    Base class for every moderation detector.
    Handles lazy model loading and execution timing.
    """

    def __init__(self, detector_type: DetectorType):
        self.detector_type = detector_type
        self.model_loaded = False

    @abstractmethod
    def load_model(self) -> None:
        """
        Load the underlying AI model.
        """
        raise NotImplementedError

    @abstractmethod
    def detect(
        self,
        request: DetectionRequest,
    ) -> DetectionResult:
        """
        Perform inference on the supplied media.
        """
        raise NotImplementedError

    def cleanup(self) -> None:
        """
        Release resources.
        Override if your detector allocates GPU memory,
        opens files, etc.
        """
        pass

    def ensure_model_loaded(self) -> None:
        """
        Lazily load the model once.
        """
        if not self.model_loaded:
            self.load_model()
            self.model_loaded = True

    def measure(
        self,
        request: DetectionRequest,
    ) -> DetectionResult:
        """
        Execute detector while measuring runtime.
        """

        self.ensure_model_loaded()

        start = perf_counter()

        try:
            result = self.detect(request)

        except Exception as exc:
            result = ResultBuilder.failed(
                detector=self.detector_type,
                error=str(exc),
            )

        result.processing_time_ms = (
            perf_counter() - start
        ) * 1000

        return result

    def __str__(self) -> str:
        return self.detector_type.value