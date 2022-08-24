from datetime import datetime

from py_types.zeromq import ZeroMQMsgBody


class RandomDataMsgBody(ZeroMQMsgBody):
    dt: datetime
    VA: float
    VB: float
    VC: float
    IA: float
    IB: float
    IC: float
    freq: float
