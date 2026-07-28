# app/core/logger/logger.py
import logging
from pathlib import Path

from app.core.logger.formatter import (
    FliqzFormatter,
)

from app.core.logger.context import (
    ContextFilter,
)


LOG_DIR = Path("logs")

LOG_DIR.mkdir(
    exist_ok=True
)


def get_logger(
    name: str
) -> logging.Logger:
    """
    Create or retrieve application logger.

    Args:
        name:
            Service name.

    Example:

        logger = get_logger(
            "minor_worker"
        )

    """


    logger = logging.getLogger(
        name
    )


    # Prevent duplicate handlers
    if logger.handlers:
        return logger



    logger.setLevel(
        logging.INFO
    )


    formatter = FliqzFormatter()


    context_filter = ContextFilter()



    # Console Handler

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(
        formatter
    )

    console_handler.addFilter(
        context_filter
    )



    # File Handler

    file_handler = logging.FileHandler(
        LOG_DIR / f"{name}.log",
        encoding="utf-8"
    )

    file_handler.setFormatter(
        formatter
    )

    file_handler.addFilter(
        context_filter
    )



    logger.addHandler(
        console_handler
    )

    logger.addHandler(
        file_handler
    )


    logger.propagate = False


    return logger