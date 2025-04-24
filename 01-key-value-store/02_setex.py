#!/usr/bin/env python3
"""Practice Redis SETEX command"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from redis_utils import get_redis_connection

redis_conn = get_redis_connection()

# SETEX - SET with expiration in seconds (atomic operation)
redis_conn.setex("session:auth", 30, "user:12345")
ttl = redis_conn.ttl("session:auth")
value = redis_conn.get("session:auth")

print(f"SETEX session:auth 30 'user:12345'")
print(f"TTL session:auth = {ttl}")
print(f"GET session:auth = {value}")

# Compared to regular SET with EX
redis_conn.set("session:login", "active", ex=45)
ttl = redis_conn.ttl("session:login")
value = redis_conn.get("session:login")

print(f"\nSET session:login 'active' EX 45")
print(f"TTL session:login = {ttl}")
print(f"GET session:login = {value}")