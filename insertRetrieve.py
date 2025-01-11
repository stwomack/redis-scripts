from dotenv import load_dotenv
import redis
import random
import os

load_dotenv()  # Load environment variables from .env

REDIS_CE_HOST = os.environ.get('REDIS_CE_HOST')
REDIS_CE_PASSWORD = os.environ.get('REDIS_CE_PASSWORD')
REDIS_ENTERPRISE_HOST = os.environ.get('REDIS_ENTERPRISE_HOST')

# Connect to Redis
rce = redis.Redis(host=REDIS_CE_HOST, port=6379, db=0, password=REDIS_CE_PASSWORD)
re = redis.Redis(host=REDIS_ENTERPRISE_HOST, port=18874)

# Insert values 1-100 into a Sorted Set
for i in range(1, 101):
    print(f"Inserting number: {i}")
    rce.zadd('my_numbers_ordered', {i: i})

# Retrieve values in reverse order from the 'my_numbers_ordered' Sorted Set
ordered_values_reversed = re.zrevrange('my_numbers_ordered', 0, -1)

# Print the values
print("Ordered Values in reverse order:")
for value in ordered_values_reversed:
    print(value.decode('utf-8'))

# Insert 100 random values into another Sorted Set
random_values = set()  # Use a set to ensure unique random values
while len(random_values) < 100:
    random_values.add(random.randint(1, 1000))  # Generate random integers within a range
for value in random_values:
    print(f"Inserting random value: {value}")
    rce.zadd('my_numbers_random', {value: value})

# Retrieve values in reverse order from the 'my_numbers_random' Sorted Set
random_values_reversed = re.zrevrange('my_numbers_random', 0, -1)

print("\nRandom Values in reverse order:")
for value in random_values_reversed:
    print(value.decode('utf-8'))