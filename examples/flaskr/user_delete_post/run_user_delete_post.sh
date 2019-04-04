#!/usr/bin/env bash


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PARENT_DIR="${DIR}/.."
echo ${PARENT_DIR}
source ${PARENT_DIR}/env.sh
locust
