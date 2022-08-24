from typing import TypedDict


class ZeroMQMsgBody(TypedDict):
    pass


class ZeroMQMsg(TypedDict):
    msg_origin: str
    msg_type: str
    msg_body: ZeroMQMsgBody


class ZeroMQDsn:
    @staticmethod
    def build(ipv4: str, port: str) -> str:
        return f"tcp://{ipv4}:{port}"
