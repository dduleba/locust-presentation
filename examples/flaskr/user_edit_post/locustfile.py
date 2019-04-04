import time

from examples.flaskr.user_add_post.locustfile import UserAddPostTaskSet
from examples.flaskr.user_login.locustfile import UserLoginTaskSet
from examples.flaskr.user_register.locustfile import UserRegisterTaskSet
from examples.flaskr.utils import _get_post_id
from locust import HttpLocust, TaskSet, task


class UserEditPostTaskSet(TaskSet):

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
        title = '{}: title'.format(self.user_name)
        body = "to be updated"

        response = UserAddPostTaskSet.user_add_post(client=self.client,
                                                    title=title,
                                                    body=body,
                                                    catch_response=True)
        self.post_id = _get_post_id(response.content)

    @task()
    def edit(self):
        if self.post_id is None:
            return
        self.client.post(
            '/{post_id}/update'.format(post_id=self.post_id),
            data={'title': 'updated task {}'.format(time.time()),
                  'body': '''updated body
                      with content
                      {}
                      '''.format(time.time())
                  },
            name='/[post_id]/update'
        )


class IndexLocust(HttpLocust):
    task_set = UserEditPostTaskSet
    min_wait = 5000
    max_wait = 10000
    host = 'http://127.0.0.1:5000'
