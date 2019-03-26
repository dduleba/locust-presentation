import time

from locust import HttpLocust, task, TaskSequence, seq_task


class LoggedUserSequence(TaskSequence):

    def on_start(self):
        self.prefix = id(self)
        self.user_id = 0
        print(self.prefix)
        self.user_name = 'test_user_{}_{}'.format(self.prefix, self.user_id)
        self.user_password = 'test_password_{}_{}'.format(self.prefix, self.user_id)
        self.client.post(
            "/auth/register",
            data={
                'username': self.user_name,
                'password': self.user_password
            }
        )

    @seq_task(1)
    def login(self):
        self.client.post(
            "/auth/login",
            data={
                'username': self.user_name,
                'password': self.user_password
            }
        )

    @seq_task(2)
    @task(5)
    def new(self):
        self.client.post(
            "/create",
            data={
                'title': '{}: {} title'.format(self.user_name, self.user_id),
                'body': "my body text"
            }
        )

    def _get_post_id(self):
        with self.client.get('/', catch_response=True) as response:
            if response.status_code == 200:
                # <a class="action" href="/2/update">Edit</a>
                content = response.content.decode()
                end_index = content.index('/update')
                start_index = content[:end_index].rindex('/') + 1
                return content[start_index:end_index]
            else:
                response.failure('Wrong list index response code: {}'.format(response.status_code))

    @seq_task(3)
    @task(2)
    def edit(self):
        post_id = self._get_post_id()
        if post_id is None:
            return
        self.client.post(
            '/{post_id}/update'.format(post_id=post_id),
            data={'title': 'updated task {}'.format(time.time()),
                  'body': '''updated body
                  with content
                  '''
                  },
            name='/[post_id]/update'
        )

    @seq_task(3)
    def delete(self):
        post_id = self._get_post_id()
        self.client.post(
            '/{post_id}/delete'.format(post_id=post_id),
            name='/[post_id]/delete'
        )

    @seq_task(4)
    def logout(self):
        self.client.get(
            "/auth/logout",
        )


class LoggedLocust(HttpLocust):
    task_set = LoggedUserSequence
    min_wait = 5000
    max_wait = 5000
    host = 'http://127.0.0.1:5000'
