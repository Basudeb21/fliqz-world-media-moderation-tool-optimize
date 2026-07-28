import logging
from contextvars import ContextVar
from typing import Optional


# Stores current execution context.
# Works safely with:
# - Threads
# - Async tasks
# - Workers

_log_context: ContextVar[dict] = ContextVar(
    "log_context",
    default={}
)



def set_log_context(
    **kwargs
) -> None:
    """
    Set logging context values.

    Example:

    set_log_context(
        attachment_id=101,
        chunk_id=5
    )
    """

    current = _log_context.get().copy()

    current.update(kwargs)

    _log_context.set(
        current
    )



def clear_log_context() -> None:
    """
    Remove current context.
    """

    _log_context.set({})



def get_log_context() -> dict:
    """
    Return current context.
    """

    return _log_context.get()



class ContextFilter(logging.Filter):
    """
    Injects context values into log records.

    Formatter can directly access:

    record.attachment_id
    record.chunk_id
    record.worker_id
    """


    def filter(
        self,
        record: logging.LogRecord
    ) -> bool:

        context = get_log_context()


        record.attachment_id = context.get(
            "attachment_id",
            "-"
        )

        record.chunk_id = context.get(
            "chunk_id",
            "-"
        )

        record.worker_id = context.get(
            "worker_id",
            "-"
        )

        record.service = context.get(
            "service",
            "SYSTEM"
        )


        return True