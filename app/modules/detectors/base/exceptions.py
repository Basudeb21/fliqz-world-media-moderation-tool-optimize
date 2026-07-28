# app/modules/detectors/base/exceptions.py
"""
Detector exception hierarchy.
All detector-related exceptions should inherit from DetectorError.
"""

class DetectorError(Exception):
    """
    Base exception for all detector errors.
    """
    pass


class ModelLoadError(DetectorError):
    """
    Raised when an AI model cannot be loaded.
    """
    pass


class InferenceError(DetectorError):
    """
    Raised when model inference fails.
    """
    pass


class InvalidMediaError(DetectorError):
    """
    Raised when the supplied media is invalid.
    """
    pass


class UnsupportedMediaError(DetectorError):
    """
    Raised when the detector does not support
    the provided media type.
    """
    pass


class DetectorCancelledError(DetectorError):
    """
    Raised when a running detector is cancelled.
    """
    pass


class DetectorConfigurationError(DetectorError):
    """
    Raised when detector configuration is invalid.
    """
    pass


class EvidenceGenerationError(DetectorError):
    """
    Raised when evidence generation fails.
    """
    pass