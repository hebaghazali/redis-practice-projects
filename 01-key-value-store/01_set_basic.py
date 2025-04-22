#!/usr/bin/env python3
"""Practice Redis SET command"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from redis_utils import get_redis_connection

redis_conn = get_redis_connection()

# Basic SET and GET
redis_conn.set("user:name", "John Doe")
result = redis_conn.get("user:name")
print(f"SET user:name 'John Doe'\nGET user:name = {result}")

# SET with expire (EX) in seconds
redis_conn.set("session:id", "abc123", ex=30)
ttl = redis_conn.ttl("session:id")
print(f"\nSET session:id 'abc123' EX 30\nTTL session:id = {ttl}")

# SET with expire (PX) in milliseconds
redis_conn.set("temp:token", "xyz789", px=5000)
pttl = redis_conn.pttl("temp:token") 
print(f"\nSET temp:token 'xyz789' PX 5000\nPTTL temp:token = {pttl}")

# SET with KEEPTTL flag
redis_conn.set("preserve:ttl", "original", ex=60)
original_ttl = redis_conn.ttl("preserve:ttl")
redis_conn.set("preserve:ttl", "updated", keepttl=True)
new_ttl = redis_conn.ttl("preserve:ttl")
print(f"\nSET preserve:ttl 'original' EX 60\nOriginal TTL: {original_ttl}")
print(f"SET preserve:ttl 'updated' KEEPTTL\nNew TTL: {new_ttl}")