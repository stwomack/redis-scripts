from dotenv import load_dotenv
import redis
import random
import os

load_dotenv()  # Load environment variables from .env

REDIS_CE_HOST = os.environ.get('REDIS_CE_HOST')
REDIS_CE_PASSWORD = os.environ.get('REDIS_CE_PASSWORD')
REDIS_ENTERPRISE_HOST = os.environ.get('REDIS_ENTERPRISE_HOST')

# Connect to Redis CE (source)
redis_ce = redis.Redis(host=REDIS_CE_HOST, port=6379, db=0, password=REDIS_CE_PASSWORD)

# Connect to Redis Enterprise (replica)
redis_enterprise = redis.Redis(host=REDIS_ENTERPRISE_HOST, port=18874, db=0)

# Use a sorted set for efficient insertion and retrieval of ordered data
key_name = "random_values"

# Insert 100 random values into Redis CE using ZADD (sorted set add)
for _ in range(100):
    random_value = random.randint(1, 1000)  # Generate random integer
    print(f"Inserting Key: {random_value}")
    redis_ce.zadd(key_name, {str(random_value): random_value})

# Retrieve values in reverse order from Redis Enterprise using ZREVRANGE
values = redis_enterprise.zrevrange(key_name, 0, -1)

# Print the values in reverse order
for value in values:
    print(f"Retrieving Value: {value.decode('utf-8')}")