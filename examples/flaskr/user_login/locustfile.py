from examples.flaskr import user_register
from examples.flaskr.user_register.locustfile import UserRegisterTaskSet
from locust import HttpLocust, TaskSet, task


class UserLoginTaskSet(TaskSet):

    def on_start(self):
        user_id = id(self)
        self.user_name = 'test_user_{}'.format(user_id)
        self.user_password = 'test_user_password_{}'.format(user_id)
        UserRegisterTaskSet.user_register(client=self.client,
                                          user_name=self.user_name,
                                          user_password=self.user_password)

    @staticmethod
    def user_login(client, user_name, user_password):
        client.post(
            "/auth/login",
            data={
                'username': user_name,
                'password': user_password
            }
        )

    @task()
    def login(self):
        self.user_login(client=self.client,
                        user_name=self.user_name,
                        user_password=self.user_password)




class IndexLocust(HttpLocust):
    task_set = UserLoginTaskSet
    min_wait = 5000
    max_wait = 10000
    host = 'http://127.0.0.1:5000'
