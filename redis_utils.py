"""
Redis Connection Utility

This module provides a standardized way to connect to Redis across all practice projects.
It automatically selects the correct database based on the project directory.
"""

import os
import redis
import socket
import time

# Map project directories to their respective Redis database numbers
PROJECT_DB_MAP = {
    "01-key-value-store": 0,
    "02-page-cache": 1,
    "03-user-profiles-hash": 2,
    "04-session-auth-system": 3,
    "05-follow-system-set": 4,
    "06-likes-system": 5,
    "07-leaderboard-zset": 6,
    "08-bidding-system-tx": 7,
    "09-lua-custom-ops": 8,
    "10-locking-system": 9,
    "11-fulltext-search-redisearch": 10,
    "12-stream-pipeline": 11,
}

def get_redis_connection(host='localhost', port=6379, password=None, auto_detect_db=True, max_retries=3):
    """
    Get a Redis connection for the current project.
    
    Args:
        host (str): Redis host address
        port (int): Redis port
        password (str): Redis password, if any
        auto_detect_db (bool): If True, automatically select database based on current directory
        max_retries (int): Maximum number of connection retries
        
    Returns:
        redis.Redis: A configured Redis client instance
    """
    db = 0  # Default to db 0
    
    if auto_detect_db:
        # Try to detect current project directory
        current_path = os.path.abspath(os.getcwd())
        for project_dir, db_num in PROJECT_DB_MAP.items():
            if project_dir in current_path:
                db = db_num
                print(f"Using Redis database {db} for {project_dir}")
                break
    
    # Try to establish connection with retries
    retry_count = 0
    while retry_count < max_retries:
        try:
            print(f"Connecting to Redis at {host}:{port} (database {db})...")
            r = redis.Redis(
                host=host,
                port=port,
                db=db,
                password=password,
                decode_responses=True,  # For convenience: automatically decode bytes to strings
                socket_timeout=5,       # Socket timeout in seconds
                socket_connect_timeout=5 # Connection timeout
            )
            
            # Test the connection with a simple ping
            if r.ping():
                print(f"Successfully connected to Redis!")
                return r
            
        except (redis.exceptions.ConnectionError, socket.error) as e:
            retry_count += 1
            if retry_count >= max_retries:
                print(f"Failed to connect to Redis after {max_retries} attempts.")
                print(f"Error: {e}")
                print(f"Make sure Redis is running at {host}:{port}")
                raise
            
            print(f"Connection attempt {retry_count} failed. Retrying in 1 second...")
            time.sleep(1)

# Example usage
if __name__ == "__main__":
    # This will automatically connect to the appropriate database
    # based on which project directory you're in
    try:
        r = get_redis_connection()
        print(f"Connected to Redis!")
        
        # Try a simple operation
        r.set("test_key", "It works!")
        print(f"Test value: {r.get('test_key')}")
    except Exception as e:
        print(f"Could not connect to Redis: {e}")