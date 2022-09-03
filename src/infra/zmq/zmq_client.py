# import time
import os
from typing import Callable, Optional
import logging
import json


import zmq

from py_types import ZeroMQMsg, ZeroMQDsn

logger = logging.getLogger(__name__)


MSG_TYPES = {
    "generated": bytes("Received Generated Data", "utf-8"),
}


class ZMQClient:
    def __init__(
        self,
        ipv4: str = os.environ["ZMQ_SUBS_IPV4"],
        port: str = os.environ["ZMQ_SUBS_PORT"],
        callback: Optional[Callable] = None,
        args: tuple = (),
        kwargs: dict = {},
    ):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        topic_filter = ""
        self.socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)

        self.keep_running = True
        self.cnxn_str = ZeroMQDsn.build(ipv4, port)

        # Callback
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def _connect(self) -> None:
        try:
            self.socket.connect(self.cnxn_str)
        except Exception as e:
            logger.warning(str(e))

    def _filter_msg(self, publisher_msg: str) -> Optional[ZeroMQMsg]:
        msg: ZeroMQMsg = json.loads(publisher_msg)
        if msg["msg_origin"] == "client":
            msg_type = msg["msg_type"].lower()
            client_response = MSG_TYPES.get(msg_type)
            if client_response is not None:
                return msg
            else:
                logger.warning(
                    "Received an invalid message from server: {}".format(msg)
                )
        else:
            logger.warning("Received unexpected message from server: {}".format(msg))

    def _handle(self, publisher_msg: str) -> None:
        try:
            msg = self._filter_msg(publisher_msg)
            if self.callback is not None:
                self.callback(msg, *self.args, **self.kwargs)
        except Exception as e:
            logger.warning(str(e))

    def run(self) -> None:
        self._connect()
        if not self.keep_running:
            publisher_msg = self.socket.recv_string()
            self._handle(publisher_msg)
            return

        while True:
            publisher_msg = self.socket.recv_string()
            self._handle(publisher_msg)
