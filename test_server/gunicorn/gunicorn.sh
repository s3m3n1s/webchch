#!/bin/sh
gunicorn -b 0.0.0.0:8080 -k uvicorn.workers.UvicornWorker flask_app:app
