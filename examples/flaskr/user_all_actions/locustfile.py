from examples.flaskr.posts_list.locustfile import IndexTaskSet
from examples.flaskr.user_add_post.locustfile import UserAddPostTaskSet
from examples.flaskr.user_delete_post.locustfile import UserDeletePostTaskSet
from examples.flaskr.user_edit_post.locustfile import UserEditPostTaskSet
from examples.flaskr.user_login.locustfile import UserLoginTaskSet
from examples.flaskr.user_register.locustfile import UserRegisterTaskSet
from locust import HttpLocust, TaskSet


class UserAllTaskSet(TaskSet):
    tasks = {UserEditPostTaskSet: 4,
             UserAddPostTaskSet: 4,
             UserDeletePostTaskSet: 3,
             UserLoginTaskSet: 2,
             UserRegisterTaskSet: 1,
             IndexTaskSet: 8}


class IndexLocust(HttpLocust):
    task_set = UserAllTaskSet
    min_wait = 5000
    max_wait = 10000
    host = 'http://127.0.0.1:5000'
