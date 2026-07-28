from app.core.logger.logger import (
    get_logger
)

from app.core.logger.context import (
    set_log_context,
    clear_log_context,
)



def test_logger():

    logger = get_logger(
        "test_service"
    )


    set_log_context(
        service="TestService",
        attachment_id=101,
        chunk_id=5,
        worker_id="worker01"
    )


    logger.info(
        "Testing logger"
    )


    clear_log_context()