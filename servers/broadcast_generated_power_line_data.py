from typing import List
import sys

from utils import (
    factory_zmq_context,
    generate_senoidal_data,
    send_msg,
    senoidal_data_args_to_kwargs,
)


def main(args: List[str]) -> None:
    kwargs = senoidal_data_args_to_kwargs(args)
    _, socket = factory_zmq_context()
    for msg in generate_senoidal_data(**kwargs):
        send_msg(socket, msg)


if __name__ == "__main__":
    main(sys.argv)
