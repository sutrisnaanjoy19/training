import requests
from redis import Redis
from rq import Queue
from rq import Retry
import datetime
from count import count_words_at_url

def main():
    r = Redis()
    q = Queue(connection=r)
    result = q.enqueue(count_words_at_url, 'http://nvie.com')
    print(result)
# Schedule job to run at 9:15, October 10th
    job = q.enqueue_at(datetime.datetime(2022, 7, 3, 20 , 1), 'say_hello')

# Schedule job to be run in 10 seconds
    job = q.enqueue_in(datetime.timedelta(seconds=10), "say_hello")

# Retry up to 3 times, failed job will be requeued immediately
    q.enqueue('say_hello', retry=Retry(max=3))

# Retry up to 3 times, with configurable intervals between retries
    q.enqueue('say_hello', retry=Retry(max=3, interval=[10, 30, 60]))

if __name__ == "__main__":
    main()