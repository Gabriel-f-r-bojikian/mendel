import multiprocessing as mp
import logging

from configs import LOG_CONFIGS
from processes import zmq_process

logging.basicConfig(**LOG_CONFIGS)
logger = logging.getLogger(__name__)


def main():
    try:
        # Create processes
        mp_zeromq = mp.Process(
            target=zmq_process,
            # args=(),
        )

        mp_zeromq.start()

        mp_zeromq.join()

    except Exception as e:
        logger.warning(str(e))


if __name__ == "__main__":
    main()
