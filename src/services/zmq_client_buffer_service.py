import os
import uuid
from struct import pack as struct_pack
from datetime import datetime

from py_types import Buffer, ZeroMQMsg

dirname = "/maxwell-data-processor/output-data"
file_name =  f"{uuid.uuid1()}-data-storage.dat"
file_path = os.path.join(dirname, file_name)

ZMQ_CLIENT_BUFFER = Buffer(
    dt=[],
    VA=[],
    VB=[],
    VC=[],
    IA=[],
    IB=[],
    IC=[],
)
FORMAT = "%Y-%m-%d %H:%M:%S"


def zmq_client_buffer_service(msg: ZeroMQMsg):
    dt = msg["msg_body"]["dt"]
    print(
        f"[{datetime.now().strftime(FORMAT)}]"
        f"Length: {str(len(ZMQ_CLIENT_BUFFER.VA)).zfill(2)} | Receiving: {datetime.utcfromtimestamp(dt).isoformat()}"
    )
    ZMQ_CLIENT_BUFFER.dt.append(msg["msg_body"]["dt"])
    ZMQ_CLIENT_BUFFER.VA.append(msg["msg_body"]["VA"])
    ZMQ_CLIENT_BUFFER.VB.append(msg["msg_body"]["VB"])
    ZMQ_CLIENT_BUFFER.VC.append(msg["msg_body"]["VC"])
    ZMQ_CLIENT_BUFFER.IA.append(msg["msg_body"]["IA"])
    ZMQ_CLIENT_BUFFER.IB.append(msg["msg_body"]["IB"])
    ZMQ_CLIENT_BUFFER.IC.append(msg["msg_body"]["IC"])
    # freq: float

    if 32 <= len(ZMQ_CLIENT_BUFFER.VA):
        # Remove first value
        dt_o = ZMQ_CLIENT_BUFFER.dt.pop(0)
        VA_o = ZMQ_CLIENT_BUFFER.VA.pop(0)
        VB_o = ZMQ_CLIENT_BUFFER.VB.pop(0)
        VC_o = ZMQ_CLIENT_BUFFER.VC.pop(0)
        IA_o = ZMQ_CLIENT_BUFFER.IA.pop(0)
        IB_o = ZMQ_CLIENT_BUFFER.IB.pop(0)
        IC_o = ZMQ_CLIENT_BUFFER.IC.pop(0)

        with open(file_path, "ab") as new_file:
            new_file.write(struct_pack("7d", dt_o,VA_o ,VB_o ,VC_o ,IA_o, IB_o, IC_o))
