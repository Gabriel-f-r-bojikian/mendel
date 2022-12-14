import logging

from configs import LOG_CONFIGS
from processes import zmq_process
from services import FileBufferService

logging.basicConfig(**LOG_CONFIGS)
logger = logging.getLogger(__name__)


def main():
    try:
        file_buffer_service = FileBufferService()
        zmq_process(file_buffer_service.writer)
        
    except Exception as e:
        logger.warning(str(e))


if __name__ == "__main__":
    main()
