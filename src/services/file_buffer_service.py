from io import BufferedWriter
import os
import uuid
from struct import pack as struct_pack
from datetime import datetime

from pytz import timezone
import logging

from py_types import ZeroMQMsg
from configs import configs

class FileBufferService:
    # Object properties
    file_path: str
    file_buffer: BufferedWriter
    # Private variables
    __dirname = configs.ROOT_DIR
    __format: str = "%F_%H-%M-%S.%f_UTC%Z"
    __timezone = timezone('America/Sao_Paulo')
    __logger: logging.Logger = logging.getLogger(__file__)
    logging.basicConfig(level=logging.INFO)

    def __init__(self):
        self.openNewFile()
    
    def __exit__(self):
        self.closeCurrentFile()
    
    def writer(self, msg: ZeroMQMsg):
        dt = msg["msg_body"]["dt"]
        va = msg["msg_body"]["VA"]
        vb = msg["msg_body"]["VB"]
        vc = msg["msg_body"]["VC"]
        vN = msg["msg_body"]["VN"]
        ia = msg["msg_body"]["IA"]
        ib = msg["msg_body"]["IB"]
        ic = msg["msg_body"]["IC"]
        iN = msg["msg_body"]["IN"]
        self.__logger.info(
            "[%(current_timestamp)s] Receiving: %(faraday_timestamp)s",
            dict(
                current_timestamp=datetime.now().astimezone(self.__timezone).strftime(self.__format),
                faraday_timestamp=datetime.utcfromtimestamp(dt).strftime(self.__format),
            ),
        )
        try:
            if( datetime.now().astimezone(self.__timezone).date() > self.instantiation_datetime.date() ):
                self.__logger.warning('Got here, generating another file')
                self.closeCurrentFile()
                self.openNewFile()

            self.file_buffer.write(struct_pack("9d", dt, va, vb, vc, vN, ia, ib, ic, iN))
        except Exception as e:
            self.__logger.error(e)
            raise Exception("Couldn't write on file, exiting service") from e

    def openNewFile(self):
        self.instantiation_datetime = datetime.now().astimezone(self.__timezone)
        self.inst_datetime_string = self.instantiation_datetime.strftime(self.__format)

        file_name = f"{str(self.inst_datetime_string)}.dat"
        self.file_path = os.path.join(self.__dirname, file_name)
        self.file_buffer = open(self.file_path, "ab")

    def closeCurrentFile(self):
        self.file_buffer.flush()
        self.file_buffer.close()