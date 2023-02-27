##  Registration component of service discovery


This little piece of code uses the Redis Cache Python client library to interact with Azure Redis.
The code uses `redis-py` package https://github.com/redis/redis-py.
The Redis client object is created using the connection details, including the Redis host, access key, and SSL configuration.

The `check_and_create_channel()` function is defined to check if a Redis channel exists using the `exists()` method of the Redis client.
If the channel exists, it prints a message to the console. 
If the channel doesn't exist, it creates the channel using the `execute_command()` method of the Redis client with the PUBLISH command, and prints a message to the console.

The `register_service()` function is defined to publish the service details to the Redis channel using the `publish()` method of the Redis client.
The service details are stored in a dictionary object and converted to a string using the `str()` method.

The while loop in the `register_service()` function is used to retry the Redis connection in case of a `ConnectionError` exception.
This ensures that the service registration process is reliable and fault-tolerant.

Please note that this code assumes that the Azure Redis connection details are stored in environment variables `REDIS_HOST` and `REDIS_KEY`.
These can be set in a `.env` file or in the system environment variables.

[TODO] compose TF code to deploy simple instance of Azure Redis

This code can be run on the server side of a microservice architecture to check if a Redis channel exists and create it if it doesn't, and then register the service for discovery using Azure Redis Pub/Sub.
This ensures that the Redis channel is available for publishers and subscribers to use, and that the service is discoverable by other services - example of which can be located at the root of this repo.

[TODO] add requirements file

Manula deployment procedure can be found here: https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-python-get-started
