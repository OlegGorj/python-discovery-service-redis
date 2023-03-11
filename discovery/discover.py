import json
import os
import redis

# Azure Redis connection details
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_KEY = os.environ['REDIS_KEY']

# Channel name
CHANNEL_NAME = 'my_channel'


# TODO implement frm_url method

# Redis client object
redis_client = redis.Redis(host=REDIS_HOST, port=6380, password=REDIS_KEY, ssl=True)


def is_valid_json(data):
    try:
        json.loads(data)
    except json.JSONDecodeError:
        return False
    return True


def check_and_subscribe_channel(channel_name):
    """Checks if the specified Redis channel exists, and subscribes to it if it does.
    """

    pubsub = redis_client.pubsub()

    if redis_client.exists(channel_name):

        pubsub.subscribe(channel_name)

        print(f"Subscribed to Redis channel '{channel_name}'.")

        for message in pubsub.listen():
            if message['type'] == 'message':
                print(f"Received message: {message}")

                # confirm that payload is json
                if is_valid_json(message["data"]):
                    data = json.loads(message["data"])
                else:
                    print("Invalid JSON data")
                    return

                # try to Decode the message from bytes to string
                service_details_json = message["data"].decode("utf-8")
                # Parse the JSON string to a dictionary
                service_details = json.loads(service_details_json)
                # Process the service details as needed
                print("Received service details:", service_details)

    else:
        print(f"Redis channel '{channel_name}' does not exist.")


# Check if the Redis channel exists and subscribe to it if it does
check_and_subscribe_channel(CHANNEL_NAME)
