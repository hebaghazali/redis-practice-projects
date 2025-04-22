# Redis Practice Projects

A collection of projects for learning and practicing Redis data structures and patterns.

## Project Structure

This repository contains multiple independent projects for practicing different Redis concepts:

| Project | Description |
|---------|-------------|
| 01-key-value-store | Basic string operations (SET, GET, DEL, TTL, INCR) |
| 02-page-cache | Expiration, cache pattern for e-commerce pages |
| 03-user-profiles-hash | Hashes for storing user profiles |
| 04-session-auth-system | Session tokens using hashes + TTL |
| 05-follow-system-set | Social graph using sets (follow/unfollow) |
| 06-likes-system | Count & display likes using sets |
| 07-leaderboard-zset | Leaderboard system using sorted sets |
| 08-bidding-system-tx | Bidding, atomicity with transactions |
| 09-lua-custom-ops | Lua scripting to perform atomic view count update |
| 10-locking-system | Distributed lock with EXPIRE + Lua |
| 11-fulltext-search-redisearch | RediSearch example with TF-IDF |
| 12-stream-pipeline | Redis streams with consumer groups |

## Setup Instructions

### Prerequisites

- Docker and Docker Compose
- Python 3.x
- Redis Python client (`pip install redis`)

### Running Redis

This project uses a shared Redis container for all practice examples, with database isolation. To start Redis:

```bash
docker-compose up -d
```

This will start a Redis server accessible at `localhost:6379`.

### Database Isolation

Each practice project uses a different Redis database number to prevent interference:

- See `redis-config.md` for the mapping of projects to database numbers
- Use the provided `redis_utils.py` utility to automatically connect to the correct database

### Using the Helper Utility

In your project files, you can use the helper utility to connect to Redis:

```python
# Import the utility
import sys
sys.path.append('..')  # Add parent directory to path
from redis_utils import get_redis_connection

# Get a Redis connection (automatically selects the right database)
redis_client = get_redis_connection()

# Use Redis as normal
redis_client.set('key', 'value')
```

## Running Individual Projects

Navigate to each project directory and run the Python file:

```bash
cd 01-key-value-store
python main.py
```

## Redis CLI Access

To access the Redis CLI directly:

```bash
docker exec -it redis-practice redis-cli
```

To switch databases (example: accessing database for project 06):

```bash
SELECT 5
```

## Additional Resources

- [Redis Documentation](https://redis.io/documentation)
- [Redis Python Client](https://github.com/redis/redis-py)