import redis
import random

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Create a Python set with 100 unique random integers
my_set = set()
while len(my_set) < 100:
    my_set.add(str(random.randint(0, 1000)))

# Create a dictionary to store elements with scores
# (Here, we'll use the element itself as the score)
sorted_set_data = {member: member for member in my_set}

# Add the elements to the Redis Sorted Set
r.zadd("my_redis_sorted_set", sorted_set_data)

# Retrieve the Sorted Set in descending order
# (highest score first)
reversed_sorted_set = r.zrevrange("my_redis_sorted_set", 0, -1)

# Print the reversed Sorted Set
print("Retrieved Sorted Set from Redis (Reversed):", reversed_sorted_set)

# Close the Redis connection
r.close()