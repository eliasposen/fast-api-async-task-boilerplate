import random
import time

from redis import Redis
from rq import Queue

queue = Queue(connection=Redis())


def task(sleep_time: str) -> float:
    time.sleep(sleep_time)

    return random.random()
