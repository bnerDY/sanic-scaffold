#!/usr/bin/env bash


set -e

export PYTHONUNBUFFERED=1

cd /src

if [ ${SPIDER_RUNTIME_MODE} = "test" ]; then
    exec python -m pytest
else
    exec python app.py
#    exec gunicorn --config service/gunicorn.py app:app --worker-class sanic.worker.GunicornWorker
fi
