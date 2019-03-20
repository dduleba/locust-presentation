import logging

from locust import Locust, TaskSet, task

log = logging.getLogger('my')


class MobileUserClient(TaskSet):
    @task
    def my_task(self):
        log.info("executing mobile client {}".format(self.locust))


class WebUserClient(TaskSet):

    @task
    def my_task(self):
        log.info("executing Web client {}".format(self.locust))


wait_time = 5000


class WebUserLocust(Locust):
    weight = 9
    task_set = WebUserClient
    min_wait = wait_time
    max_wait = wait_time


class MobileUserLocust(Locust):
    weight = 1
    task_set = MobileUserClient
    min_wait = wait_time
    max_wait = wait_time
