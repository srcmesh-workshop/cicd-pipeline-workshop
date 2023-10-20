import os
import redis
from flask import Flask, request, abort

app = Flask(__name__)

# read from env variables
redis_host = os.environ.get("REDIS_HOST")
if not redis_host:
    raise ValueError("Require environment variable REDIS_HOST")

redis_port = os.environ.get("REDIS_PORT")
if not redis_port:
    raise ValueError("Require environment variable REDIS_PORT")

# init redis client
redis_client = redis.Redis(host=redis_host,port=redis_port)

# REST API routes
@app.route("/insert/<key>/<value>", methods=["GET"])
def insert(key, value):
    redis_client.set(key, value)
    return "OK"

@app.route("/get/<key>", methods=["GET"])
def get(key):
    value = redis_client.get(key)
    if value is None:
        abort(404)
    return value

if __name__ == "__main__":
    app.run()
