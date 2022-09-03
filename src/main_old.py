import logging

from configs import LOG_CONFIGS
from processes import zmq_process
from services import zmq_client_buffer_service

logging.basicConfig(**LOG_CONFIGS)
logger = logging.getLogger(__name__)


def main():
    try:
        zmq_process(zmq_client_buffer_service)
    except Exception as e:
        logger.warning(str(e))


if __name__ == "__main__":
    main()
