from typing import TypedDict

class ZeroMQMsgBody(TypedDict):
    dt: float
    VA: float
    VB: float
    VC: float
    VN: float
    IA: float
    IB: float
    IC: float
    IN: float
    freq: float


class ZeroMQMsg(TypedDict):
    msg_origin: str
    msg_type: str
    msg_body: ZeroMQMsgBody


class ZeroMQDsn:
    @staticmethod
    def build(ipv4: str, port: str) -> str:
        return f"tcp://{ipv4}:{port}"
