from typing import List, NamedTuple


class Buffer(NamedTuple):
    dt: List[float]
    VA: List[float]
    VB: List[float]
    VC: List[float]
    IA: List[float]
    IB: List[float]
    IC: List[float]
