from locust import HttpLocust, TaskSet, task


class RegisterTaskSet(TaskSet):

    def on_start(self):
        self.prefix = id(self)
        self.user_id = 0
        print(self.prefix)

    @task()
    def register(self):
        self.user_id += 1
        self.client.post(
            "/auth/register",
            data={
                'username': 'test_user_{}_{}'.format(self.prefix, self.user_id),
                'password': 'test_password_{}_{}'.format(self.prefix, self.user_id)
            }
        )


class IndexLocust(HttpLocust):
    task_set = RegisterTaskSet
    min_wait = 5000
    max_wait = 5000
    host = 'http://127.0.0.1:5000'
