from infra.zmq import ZMQClient
from services import zmq_client_buffer_service


def zmq_process():
    zmq_server = ZMQClient(callback=zmq_client_buffer_service)
    zmq_server.run()
