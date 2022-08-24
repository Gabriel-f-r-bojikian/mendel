from typing import List


def senoidal_data_args_to_kwargs(args: List[str]) -> dict:
    if len(args) not in {1, 2}:
        raise Exception("You must pass { Optional[timesleep] }")

    time_sleep = 1.0 if len(args) == 1 else float(args[1])

    return dict(time_sleep=time_sleep)
