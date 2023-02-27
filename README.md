# python-discovery-service-redis

The repos hosts bunch of Python code generated as part of process of conducting PoC in order to understand best approach to designing and implementing Service Discovery mechinism using Azure Redis as backend.


## Why use Azure Redis

Well, short answer, because it looks like the right fit.


## What is Azure Redis Pub/Sub and its architecture

Azure Redis Pub/Sub is a messaging system provided by Azure Redis, which is a fully-managed in-memory data store that supports caching and real-time data processing.
Redis Pub/Sub is a publish/subscribe messaging system that allows services to publish messages to channels, and other services to subscribe to those channels to receive messages.
The system is designed to handle large numbers of messages and subscribers efficiently, making it a good choice for building scalable and fault-tolerant microservices architectures.

The architecture of Azure Redis Pub/Sub is based on three main components: publishers, subscribers, and the Redis server.

- Publishers are services that send messages to Redis channels using the `PUBLISH` command.
Publishers can publish messages to one or more channels, and each channel can have multiple publishers.

- Subscribers are services that receive messages from Redis channels using the `SUBSCRIBE` or `PSUBSCRIBE` command.
Subscribers can subscribe to one or more channels, and each channel can have multiple subscribers.

- The Redis server is the central component of the Pub/Sub system.
It stores the messages and manages the subscriptions. 
- When a publisher sends a message to a channel, the Redis server distributes the message to all subscribers of that channel.

The architecture of Azure Redis Pub/Sub is highly scalable and fault-tolerant. The Redis server can handle large numbers of messages and subscribers efficiently, and it supports clustering and replication, which can improve performance and availability. 
In addition, Redis Pub/Sub provides features such as pattern matching, which allows subscribers to receive messages from multiple channels based on a pattern, and message persistence, which allows messages to be stored in Redis and retrieved later.

According to many sources, Azure Redis Pub/Sub is a scalable and fault-tolerant messaging system that allows services to communicate using the publish/subscribe pattern.
To be completely transparent, I haven't had a chance to test how scalable and fault-tolerant it really is.
But it does make a good fit as a key component of microservice architectures, and it provides an efficient and reliable way to implement service discovery, event-driven architectures, and other real-time data processing systems.


[TODO] Analysis of HashTable architecture and its advantages.


## How do we compare Azure Redis Pub/Sub and HashTable

Azure Redis Pub/Sub is a messaging system that natively supports publish/subscribe messaging, making it a good choice for service discovery. 
With Redis Pub/Sub, services can publish their details to a Redis channel, and other services can subscribe to the channel to discover the services. 
Redis Pub/Sub is a reliable and efficient messaging system (according to Azure docs) that can handle high volumes of messages and can be used to build scalable and fault-tolerant service discovery systems.

On the other hand, using Azure Redis HashTable for service discovery requires implementing a custom solution for service registration and discovery. 
This approach can be more complex and error-prone than using Redis Pub/Sub, since it involves writing and reading data to and from a HashTable, as well as implementing a periodic update mechanism to keep the service list up-to-date. 
Also, using a HashTable for service discovery might not scale as well as Redis Pub/Sub, especially for large numbers of services, since it requires reading and writing to the HashTable for every service registration and discovery request.

In terms of performance and scalability, Redis Pub/Sub has some advantages over HashTable. 
Redis Pub/Sub is designed to handle large numbers of messages efficiently and can be used to build scalable service discovery systems. 
Redis Pub/Sub supports clustering and replication, which can improve fault tolerance and scalability. 
Redis Pub/Sub also has a lower latency than HashTable, since it doesn't involve reading and writing to a HashTable for every service discovery request.

Anyways, while it is technically possible to use Azure Redis HashTable for service discovery in Python, it seems like using Redis Pub/Sub is a better option due to its native support for messaging and scalability.
Redis Pub/Sub provides a reliable and efficient way to implement service discovery, and it is a good fit for building scalable and fault-tolerant microservice architectures.
