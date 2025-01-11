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

# Insert values 1-100 into Redis CE
for i in range(1, 101):
    print(f"Inserting Key: {i}")
    redis_ce.set(i, i)  # Use i directly as the key

# Get all keys from Redis Enterprise
keys = redis_enterprise.keys('*')

# Convert keys to integers (handling non-integer keys)
keys_int = []
for key in keys:
    try:
        keys_int.append(int(key.decode('utf-8')))
    except ValueError:
        print(f"Skipping non-integer key: {key.decode('utf-8')}")

    # Sort keys in descending order (using a sorted index)
sorted_indices = sorted(range(len(keys_int)), key=lambda k: keys_int[k], reverse=True)

# Retrieve and print keys in reverse order
for index in sorted_indices:
    print(f"Retrieving Key: {keys_int[index]}")