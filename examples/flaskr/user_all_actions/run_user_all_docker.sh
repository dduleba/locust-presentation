#!/usr/bin/env bash

docker exec locustd locust -f examples/flaskr/user_all_actions/locustfile.py
