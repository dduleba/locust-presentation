from locust import HttpLocust, TaskSet, task


class UserRegisterTaskSet(TaskSet):

    def on_start(self):
        self.prefix = id(self)
        self.user_id = 0
        print(self.prefix)

    @staticmethod
    def user_register(client, user_name, user_password):
        client.post(
            "/auth/register",
            data={
                'username': user_name,
                'password': user_password
            }
        )

    @task()
    def register(self):
        self.user_id += 1
        user_name = 'test_user_{}'.format(self.prefix, self.user_id)
        user_password = 'test_user_password_{}'.format(self.user_id)
        self.user_register(self.client, user_name, user_password)


class IndexLocust(HttpLocust):
    task_set = UserRegisterTaskSet
    min_wait = 5000
    max_wait = 10000
    host = 'http://127.0.0.1:5000'
