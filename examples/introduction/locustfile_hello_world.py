import logging

from locust import Locust, TaskSet, task

log = logging.getLogger('my')

class MyTaskSet(TaskSet):

    @task
    def my_task(self):
        log.info("executing my_task {}".format(id(self)))

class MyLocust(Locust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000