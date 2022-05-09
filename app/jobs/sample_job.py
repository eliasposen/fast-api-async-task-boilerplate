import random
import time


def sleep_job(sleep_sec: int) -> float:
    """
    Sleeps for provided number of seconds then returns a
    random float
    """
    time.sleep(sleep_sec)

    return random.random()
