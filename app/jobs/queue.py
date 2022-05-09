from redis import Redis
from rq import Queue

connection = Redis()
queue = Queue(connection=connection)
