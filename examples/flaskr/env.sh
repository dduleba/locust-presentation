#!/usr/bin/env bash

source /usr/local/bin/virtualenvwrapper.sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
SOURCE_ROOT="${DIR}/../.."
echo $SOURCE_ROOT
workon luczniczqa-locust
export PYTHONPATH=${SOURCE_ROOT}:${PYTHONPATH}