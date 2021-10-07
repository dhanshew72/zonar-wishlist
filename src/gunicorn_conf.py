bind = '0.0.0.0:8080'
# Set this to one worker so I didn't have to run into issues with my local database variable
workers = 1
# This allows gunicorn to use an ASGI server that's compatible with FastAPI
worker_class = "uvicorn.workers.UvicornWorker"
