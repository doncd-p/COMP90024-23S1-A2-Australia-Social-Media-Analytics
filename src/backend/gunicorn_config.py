# Set the number of worker processes
workers = 2

# Bind IP address and port
bind = "0.0.0.0:8080"

# Set the worker class, default is 'sync', you can also choose 'gevent' (requires installing the gevent package)
worker_class = 'sync'

# Set the worker timeout (in seconds)
timeout = 30