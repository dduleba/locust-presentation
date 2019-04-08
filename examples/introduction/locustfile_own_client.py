import logging
import random
import time

from locust import Locust, TaskSet, events, task

log = logging.getLogger()


class LoggingClient(object):

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                time.sleep(1 / random.randint(100, 1000))
                method = getattr(log, name)
                result = method(*args, **kwargs)
            except Exception as e:
                total_time = int((time.time() - start_time) * 1000)
                events.request_failure.fire(request_type="xmlrpc", name=name, response_time=total_time, exception=e)
            else:
                total_time = int((time.time() - start_time) * 1000)
                events.request_success.fire(request_type="log", name=name, response_time=total_time, response_length=0)

        return wrapper


class LoggingLocust(Locust):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = LoggingClient()


class ApiUser(LoggingLocust):
    min_wait = 100
    max_wait = 1000

    class task_set(TaskSet):
        @task(10)
        def error(self):
            self.client.error("error info")

        @task(5)
        def info(self):
            self.client.info("Test Info")
