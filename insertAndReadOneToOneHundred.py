import redis
import os

# Connect to Redis CE (source)
redis_ce = redis.Redis(host='35.193.227.53', port=6379, db=0, password='redis123')

# Connect to Redis Enterprise (replica)
redis_enterprise = redis.Redis(host='35.193.227.53', port=6379, db=0, password='redis123')

# Insert values 1-100 into Redis CE
for i in range(1, 101):
    print(f"Inserting Key: {i}")
    redis_ce.set(i, i)  # Use i directly as the key

# Get all keys from Redis Enterprise
keys = redis_enterprise.keys('*')

# Convert keys to integers
keys_int = [int(key.decode('utf-8')) for key in keys]

# Sort keys in descending order (using a sorted index)
sorted_indices = sorted(range(len(keys_int)), key=lambda k: keys_int[k], reverse=True)

# Retrieve and print keys in reverse order
for index in sorted_indices:
    print(f"Retrieving Key: {keys_int[index]}")