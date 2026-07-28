import logging


class FliqzFormatter(logging.Formatter):
    """
    Custom formatter for FliqzWorld moderation engine.

    Format example:

    2026-07-22 23:40:10 | INFO     | MinorWorker | Attachment=101 | Detection started
    """


    def format(
        self,
        record: logging.LogRecord
    ) -> str:

        timestamp = self.formatTime(
            record,
            "%Y-%m-%d %H:%M:%S"
        )

        level = record.levelname

        service = getattr(
            record,
            "service",
            "SYSTEM"
        )

        attachment_id = getattr(
            record,
            "attachment_id",
            "-"
        )

        chunk_id = getattr(
            record,
            "chunk_id",
            "-"
        )

        worker_id = getattr(
            record,
            "worker_id",
            "-"
        )

        message = record.getMessage()


        return (
            f"{timestamp} | "
            f"{level:<8} | "
            f"{service} | "
            f"attachment={attachment_id} | "
            f"chunk={chunk_id} | "
            f"worker={worker_id} | "
            f"{message}"
        )