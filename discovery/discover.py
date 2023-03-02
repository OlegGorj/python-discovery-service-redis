import os
import redis

# Azure Redis connection details
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_KEY = os.environ['REDIS_KEY']

# Channel name
CHANNEL_NAME = 'my_channel'

# Service details
SERVICE_NAME = 'my_service'     # change to env var
SERVICE_HOST = 'localhost'      # change to env var -- actual host
SERVICE_PORT = 8000             # change to env var -- 6380

# TODO implement frm_url method

# Redis client object
redis_client = redis.Redis(host=REDIS_HOST, port=6380, password=REDIS_KEY, ssl=True)


def check_and_subscribe_channel(channel_name):
    """Checks if the specified Redis channel exists, and subscribes to it if it does.
    """

    pubsub = redis_client.pubsub()

    if redis_client.exists(channel_name):
        pubsub.subscribe(channel_name)
        print(f"Subscribed to Redis channel '{channel_name}'.")
        for message in pubsub.listen():
            if message['type'] == 'message':
                print(f"Received message: {message['data']}")
    else:
        print(f"Redis channel '{channel_name}' does not exist.")


# Check if the Redis channel exists and subscribe to it if it does
check_and_subscribe_channel(CHANNEL_NAME)
