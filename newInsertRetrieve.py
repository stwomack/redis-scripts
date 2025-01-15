from dotenv import load_dotenv
import redis
import random
import os

load_dotenv()  # Load environment variables from .env

REDIS_CE_HOST = os.environ.get('REDIS_CE_HOST')
REDIS_CE_PASSWORD = os.environ.get('REDIS_CE_PASSWORD')
REDIS_CE_PORT = os.environ.get('REDIS_CE_PORT')
REDIS_ENTERPRISE_HOST = os.environ.get('REDIS_ENTERPRISE_HOST')
REDIS_ENTERPRISE_PORT = os.environ.get('REDIS_ENTERPRISE_PORT')

# Connect to Redis
rce = redis.Redis(host=REDIS_CE_HOST, port=REDIS_CE_PORT, db=0, password=REDIS_CE_PASSWORD)
re = redis.Redis(host=REDIS_ENTERPRISE_HOST, port=REDIS_ENTERPRISE_PORT)

# Add numbers 1-100 to a Redis list

# Create a list of numbers
my_list = list(range(1, 101))
print(f"My list: {my_list}")

# Add the entire list to Redis in a single operation
rce.rpush('my_list', *my_list)

# Retrieve the list and reverse it in Python
full_list = re.lrange('my_list', 0, -1)
reversed_list = full_list[::-1]

# Decode the bytes to strings
reversed_list_str = [str(item, 'utf-8') for item in reversed_list]

print(reversed_list_str)