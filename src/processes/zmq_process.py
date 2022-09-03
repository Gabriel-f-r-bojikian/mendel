from typing import Callable, Optional

from infra.zmq import ZMQClient


def zmq_process(callback: Optional[Callable] = None):
    zmq_server = ZMQClient(callback=callback)
    zmq_server.run()
