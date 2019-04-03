from random import random

import requests

# Pobranie głównej strony

r = requests.get('http://localhost:5000/')
print(r.status_code)
print(r.content)

# rejestracja użytkownika - HTTP post request
user_id = random()
username = 'test_user_{}'.format(user_id)
userpassword = 'test_user_pass_{}'.format(user_id)
r = requests.post('http://localhost:5000/auth/register',
                  data={'username': username,
                        'password': userpassword})
print(r.status_code)

# logowanie
session = requests.Session()

r = session.post('http://localhost:5000/auth/login',
                 data={'username': username,
                       'password': userpassword})
print(r.status_code)
print(session.cookies)

r=session.post('http://localhost:5000/create',
            data={'title': 'post example',
                  'body': 'witam na ŁuczniczQA meetup'})
print(r.status_code)