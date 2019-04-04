from locust import HttpLocust, TaskSet, task

class IndexTaskSet(TaskSet):
    @task()
    def index(self):
        self.client.get("/")


class IndexLocust(HttpLocust):
    task_set = IndexTaskSet
    min_wait = 5000
    max_wait = 10000
    host='http://127.0.0.1:5000'