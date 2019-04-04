from examples.flaskr.user_login.locustfile import UserLoginTaskSet
from examples.flaskr.user_register.locustfile import UserRegisterTaskSet
from locust import HttpLocust, TaskSet, task


class UserAddPostTaskSet(TaskSet):

    def on_start(self):
        user_id = id(self)
        self.user_name = 'test_user_{}'.format(user_id)
        self.user_password = 'test_user_password_{}'.format(user_id)
        UserRegisterTaskSet.user_register(client=self.client,
                                          user_name=self.user_name,
                                          user_password=self.user_password)
        UserLoginTaskSet.user_login(client=self.client,
                                    user_name=self.user_name,
                                    user_password=self.user_password)
        self.post_id = 0

    @staticmethod
    def user_add_post(client, title, body, catch_response=False):
        with client.post(
            "/create",
            data={
                'title': title,
                'body': body
            },
            catch_response=catch_response
        ) as resp:
            return resp

    @task()
    def login(self):
        self.post_id += 1
        title = '{}: title {}'.format(self.user_name, self.post_id)
        body = "my body text"
        self.user_add_post(self.client, title, body, catch_response=False)

class IndexLocust(HttpLocust):
    task_set = UserAddPostTaskSet
    min_wait = 5000
    max_wait = 10000
    host = 'http://127.0.0.1:5000'
