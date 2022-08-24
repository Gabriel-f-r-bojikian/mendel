from os.path import dirname, realpath, join
from typing import Optional
import logging

from pydantic import BaseSettings


class Configs(BaseSettings):
    LOG_PATH: Optional[str]

    class Config:
        env_file = join(dirname(realpath(__file__)), ".env")
        case_sensitive = True
        env_file = ".env"


configs = Configs()


LOG_CONFIGS = {
    "filename": "data-processor.log",
    "filemode": "a",
    "format": (
        "%(asctime)s "
        "[%(levelname)s] "
        "%(module)s-%(lineno)s-%(name)s: "
        "%(message)s"
    ),
    "level": logging.DEBUG,
    "datefmt": "%Y-%m-%dT%H:%M:%S%z",
}
