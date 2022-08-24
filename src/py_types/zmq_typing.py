from typing import TypedDict
from datetime import datetime


class ZeroMQMsgBody(TypedDict):
    dt: datetime
    VA: float
    VB: float
    VC: float
    IA: float
    IB: float
    IC: float
    freq: float


class ZeroMQMsg(TypedDict):
    msg_origin: str
    msg_type: str
    msg_body: ZeroMQMsgBody


class ZeroMQDsn:
    @staticmethod
    def build(ipv4: str, port: str) -> str:
        return f"tcp://{ipv4}:{port}"
