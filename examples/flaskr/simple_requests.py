from random import random

import requests

# Initial condition
user_id = random()
username = 'test_user_{}'.format(user_id)
userpassword = 'test_user_pass_{}'.format(user_id)

# Pobranie głównej strony
session = requests.Session()
r = session.get('http://localhost:5000/')
print('get status code: ', r.status_code)
print('get content: ', r.content[:80])

# rejestracja użytkownika - HTTP post request
r = session.post('http://localhost:5000/auth/register',
                 data={'username': username,
                       'password': userpassword})
print('register status code: ', r.status_code)

r = session.post('http://localhost:5000/auth/login',
                 data={'username': username,
                       'password': userpassword})
print('login status code: ', r.status_code)
print('login cookies: ', session.cookies)

r = session.post('http://localhost:5000/create',
                 data={'title': 'post example by {}'.format(username),
                       'body': 'witam na ŁuczniczQA meetup'})
print('post add status code: ', r.status_code)
