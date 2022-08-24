from typing import List, NamedTuple
from datetime import datetime


class Buffer(NamedTuple):
    dt: List[datetime]
    VA: List[float]
    VB: List[float]
    VC: List[float]
    IA: List[float]
    IB: List[float]
    IC: List[float]
