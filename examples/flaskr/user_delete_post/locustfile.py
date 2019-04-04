from examples.flaskr.user_add_post.locustfile import UserAddPostTaskSet
from examples.flaskr.user_login.locustfile import UserLoginTaskSet
from examples.flaskr.user_register.locustfile import UserRegisterTaskSet
from examples.flaskr.utils import _get_post_id
from locust import HttpLocust, TaskSequence, seq_task


class UserDeletePostTaskSet(TaskSequence):

    def on_start(self):
        user_id = id(self)
        self.user_name = 'test_user_{}'.format(user_id)
        self.user_password = '{}x'.format(self.user_name)
        UserRegisterTaskSet.user_register(client=self.client,
                                          user_name=self.user_name,
                                          user_password=self.user_password)
        UserLoginTaskSet.user_login(client=self.client,
                                    user_name=self.user_name,
                                    user_password=self.user_password)
        self.post_id = None

    @seq_task(1)
    def add_post(self):
        title = '{}: title'.format(self.user_name)
        body = "to be deleted"
        response = UserAddPostTaskSet.user_add_post(client=self.client,
                                                    title=title,
                                                    body=body, catch_response=True)
        self.post_id = _get_post_id(content=response.content)

    @seq_task(2)
    def delete(self):
        if self.post_id is None:
            return

        self.client.post(
            '/{post_id}/delete'.format(post_id=self.post_id),
            name='/[post_id]/delete'
        )
        self.post_id = None


class IndexLocust(HttpLocust):
    task_set = UserDeletePostTaskSet
    min_wait = 5000
    max_wait = 10000
    host = 'http://127.0.0.1:5000'
