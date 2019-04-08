#!/usr/bin/env bash

docker exec locustd pkill -f locust
docker exec locustd locust -f examples/introduction/locustfile_own_client.py