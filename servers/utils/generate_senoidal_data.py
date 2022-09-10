from datetime import datetime
from time import sleep
from typing import Iterator

import numpy as np

from py_types import ZeroMQMsg, RandomDataMsgBody

FORMAT = "%Y-%m-%d %H:%M:%S"


def generate_senoidal_data(time_sleep: float) -> Iterator[ZeroMQMsg]:
    # Arrays de tensões e correntes de fase, com harmônicas
    # n = 4001 # Numero de pontos
    f = 60  # Frequência
    f_nyquist = 6000
    samples = 1
    n = int(10 * np.ceil(f_nyquist / f))
    omega = 2.0 * np.pi * f
    t = np.linspace(0, samples / f, n)[:-1]
    dt = 1 / f_nyquist

    v_a = (
        np.sin(omega * t) + 0.5 * np.sin(3.0 * omega * t) + 0.2 * np.sin(5 * omega * t)
    )
    v_b = np.sin(omega * t - (2 * np.pi / 3))
    v_c = np.sin(omega * t + (2 * np.pi / 3))
    v_n = v_a + v_b + v_c
    i_a = np.sin(omega * t)
    i_b = np.sin(omega * t - (2 * np.pi / 3))
    i_c = np.sin(omega * t + (2 * np.pi / 3))
    i_n = i_a + i_b + i_c

    start_date = 1577836800.0
    dt_counter = start_date
    count = 0
    while True:
        msg_body = RandomDataMsgBody(
            dt=dt_counter,
            VA=v_a[count],
            VB=v_b[count],
            VC=v_c[count],
            VN=v_n[count],
            IA=i_a[count],
            IB=i_b[count],
            IC=i_c[count],
            IN=i_n[count],
            freq=f,
        )
        zmq_message: ZeroMQMsg = {
            "msg_origin": "client",
            "msg_type": "generated",
            "msg_body": msg_body,
        }
        print(f"[{datetime.now().strftime(FORMAT)}]Sending: {dt_counter}")
        yield zmq_message
        sleep(time_sleep)
        dt_counter += dt
        count += 1
        count = count % n
