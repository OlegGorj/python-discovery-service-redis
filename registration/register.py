import os
import time
import redis

# Azure Redis connection details
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_KEY = os.environ['REDIS_KEY']
REDIS_CHANNEL = 'service_discovery_channel'

# Channel name
CHANNEL_NAME = 'my_channel'

# Service details
SERVICE_NAME = 'my_service'
SERVICE_HOST = 'localhost'
SERVICE_PORT = 8000

# Redis client object
redis_client = redis.Redis(host=REDIS_HOST, port=6380, password=REDIS_KEY, ssl=True)

def check_and_create_channel(channel_name):
    """
    Checks if the specified Redis channel exists, and creates it if it doesn't.
    """
    if redis_client.exists(channel_name):
        print(f"Redis channel '{channel_name}' already exists.")
    else:
        redis_client.execute_command('PUBLISH', channel_name, 'Channel created.')
        print(f"Redis channel '{channel_name}' created.")


def register_service():
    """
    Registers the service by publishing its details to the Redis channel.
    """
    service_data = {'name': SERVICE_NAME, 'host': SERVICE_HOST, 'port': SERVICE_PORT}
    while True:
        try:
            redis_client.publish(REDIS_CHANNEL, str(service_data))
            break
        except redis.ConnectionError:
            print('Redis connection error, retrying in 5 seconds...')
            time.sleep(5)


# Check if the Redis channel exists and create it if it doesn't
check_and_create_channel(CHANNEL_NAME)

# Register the service for discovery
register_service()
