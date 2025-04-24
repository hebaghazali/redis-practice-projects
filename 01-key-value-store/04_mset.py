#!/usr/bin/env python3
"""Practice Redis MSET command"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from redis_utils import get_redis_connection

redis_conn = get_redis_connection()

# MSET - Set multiple keys to multiple values in a single operation
redis_conn.mset({
    "user:1:name": "Alice",
    "user:1:email": "alice@example.com",
    "user:1:age": "28"
})

# Get multiple values with MGET
values = redis_conn.mget("user:1:name", "user:1:email", "user:1:age")
print(f"MSET user:1:name Alice user:1:email alice@example.com user:1:age 28")
print(f"MGET user:1:name user:1:email user:1:age = {values}")

# MSETNX - Set multiple keys to multiple values, only if none of the keys exist
# First, delete existing keys
redis_conn.delete("user:2:name", "user:2:email", "user:2:age")

# This should succeed (returns True) since none of the keys exist
result1 = redis_conn.msetnx({
    "user:2:name": "Bob",
    "user:2:email": "bob@example.com",
    "user:2:age": "32"
})
print(f"\nMSETNX user:2:name Bob user:2:email bob@example.com user:2:age 32 = {result1}")

# Try again, but this time all keys already exist (should return False)
result2 = redis_conn.msetnx({
    "user:2:name": "Robert",
    "user:2:email": "robert@example.com",
    "user:2:age": "33"
})
print(f"MSETNX user:2:name Robert user:2:email robert@example.com user:2:age 33 = {result2}")

# Try with a mix of existing and non-existing keys (should still return False)
result3 = redis_conn.msetnx({
    "user:2:name": "Rob",  # Exists
    "user:2:location": "New York"  # Doesn't exist
})
print(f"MSETNX user:2:name Rob user:2:location 'New York' = {result3}")

# Check final values
values = redis_conn.mget("user:2:name", "user:2:email", "user:2:age", "user:2:location")
print(f"MGET user:2:name user:2:email user:2:age user:2:location = {values}")

# XX option example - Only set keys that already exist
print("\n# Example of using XX option with multiple SET commands")

# Create some initial keys
redis_conn.set("user:3:name", "Charlie")
redis_conn.set("user:3:email", "charlie@example.com")
# Note: user:3:location doesn't exist

print("Initial values:")
values = redis_conn.mget("user:3:name", "user:3:email", "user:3:location")
print(f"MGET user:3:name user:3:email user:3:location = {values}")

# In Redis itself, MSET doesn't support XX option
# Instead, we can use a transaction with multiple SET commands
pipe = redis_conn.pipeline()
pipe.set("user:3:name", "Charles", xx=True)
pipe.set("user:3:email", "charles@example.com", xx=True)  
pipe.set("user:3:location", "Paris", xx=True)  # This won't set as key doesn't exist
results = pipe.execute()

print("\nAfter SET with XX option in pipeline:")
print(f"Results of SET operations with XX: {results}")  # Shows [True, True, False]
values = redis_conn.mget("user:3:name", "user:3:email", "user:3:location")
print(f"MGET user:3:name user:3:email user:3:location = {values}")