#!/usr/bin/env python3
"""Practice Redis SETNX command"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from redis_utils import get_redis_connection

redis_conn = get_redis_connection()

# Clear any existing keys first
redis_conn.delete("config:max_connections", "user:profile")

# SETNX - SET if Not eXists (returns 1 if key was set, 0 if key already exists)
result1 = redis_conn.setnx("config:max_connections", "100")
value1 = redis_conn.get("config:max_connections")
print(f"SETNX config:max_connections 100 = {result1}")
print(f"GET config:max_connections = {value1}")

# Try to set the same key again with SETNX
result2 = redis_conn.setnx("config:max_connections", "200")
value2 = redis_conn.get("config:max_connections")
print(f"SETNX config:max_connections 200 = {result2}")  # Should return 0
print(f"GET config:max_connections = {value2}")  # Should still be "100"

# In Python Redis client, you can also use the nx parameter with SET
result3 = redis_conn.set("user:profile", "created", nx=True)
print(f"\nSET user:profile 'created' NX = {result3}")

# Try to set again with nx=True
result4 = redis_conn.set("user:profile", "updated", nx=True)
print(f"SET user:profile 'updated' NX = {result4}")  # Should return None

# Current value
value4 = redis_conn.get("user:profile") 
print(f"GET user:profile = {value4}")  # Should still be "created"