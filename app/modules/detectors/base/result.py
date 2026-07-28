# app/modules/detectors/base/result.py
from __future__ import annotations

from app.modules.detectors.base.schemas import (
    Detection,
    DetectionResult,
    DetectorStatus,
    DetectorType,
)


class ResultBuilder:
    """
    Helper class for creating standardized DetectionResult objects.
    """

    @staticmethod
    def success(
        detector: DetectorType,
        detections: list[Detection] | None = None,
        processing_time_ms: float = 0.0,
        metadata: dict | None = None,
    ) -> DetectionResult:

        return DetectionResult(
            detector=detector,
            status=DetectorStatus.SUCCESS,
            detections=detections or [],
            processing_time_ms=processing_time_ms,
            metadata=metadata or {},
        )

    @staticmethod
    def failed(
        detector: DetectorType,
        error: str,
        processing_time_ms: float = 0.0,
        metadata: dict | None = None,
    ) -> DetectionResult:

        return DetectionResult(
            detector=detector,
            status=DetectorStatus.FAILED,
            detections=[],
            processing_time_ms=processing_time_ms,
            metadata=metadata or {},
            error=error,
        )

    @staticmethod
    def skipped(
        detector: DetectorType,
        reason: str,
        metadata: dict | None = None,
    ) -> DetectionResult:

        return DetectionResult(
            detector=detector,
            status=DetectorStatus.SKIPPED,
            detections=[],
            metadata=metadata or {},
            error=reason,
        )