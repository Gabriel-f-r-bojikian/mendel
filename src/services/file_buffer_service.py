from io import BufferedWriter
import os
import uuid
from struct import pack as struct_pack
from datetime import datetime
# import logging

from py_types import ZeroMQMsg
from configs import configs



class FileBufferService:
    # Object properties
    file_path: str
    file_buffer: BufferedWriter
    # Private variables
    __format: str = "%Y-%m-%d %H:%M:%S"
    # __logger: logging.Logger = logging.getLogger(__file__)

    def __init__(self):
        dirname = configs.ROOT_DIR
        file_name =  f"{uuid.uuid1()}-data-storage.dat"
        self.file_path = os.path.join(dirname, file_name)
        self.file_buffer = open(self.file_path, "ab")
    
    def __exit__(self):
        self.file_buffer.flush()
        self.file_buffer.close()
    
    def writer(self, msg: ZeroMQMsg):
        dt = msg["msg_body"]["dt"]
        va = msg["msg_body"]["VA"]
        vb = msg["msg_body"]["VB"]
        vc = msg["msg_body"]["VC"]
        ia = msg["msg_body"]["IA"]
        ib = msg["msg_body"]["IB"]
        ic = msg["msg_body"]["IC"]
        # self.__logger.info(
        #     "[%(current_timestamp)s] Receiving: %(faraday_timestamp)s",
        #     dict(
        #         current_timestamp=datetime.now(),
        #         faraday_timestamp=datetime.utcfromtimestamp(dt),
        #     ),
        # )
        print(
            f"[{datetime.now().strftime(self.__format)}]"
            f" | Receiving: {datetime.utcfromtimestamp(dt).isoformat()}"
        )
        try:
            self.file_buffer.write(struct_pack("7d", dt, va, vb, vc, ia, ib, ic))
        except Exception as e:
            raise Exception("Couldn't write on file, exiting service") from e

