# Redis Database Configuration

This file tracks which Redis database is used by each practice project.

| Project Directory              | Redis DB # | Description                             |
|-------------------------------|------------|----------------------------------------|
| 01-key-value-store            | 0          | Basic string operations                 |
| 02-page-cache                 | 1          | E-commerce page caching                 |
| 03-user-profiles-hash         | 2          | User profiles using hashes              |
| 04-session-auth-system        | 3          | Authentication sessions                 |
| 05-follow-system-set          | 4          | Social graph with sets                  |
| 06-likes-system               | 5          | Likes system using sets                 |
| 07-leaderboard-zset           | 6          | Leaderboards with sorted sets           |
| 08-bidding-system-tx          | 7          | Bidding with transactions               |
| 09-lua-custom-ops             | 8          | Custom operations with Lua scripting    |
| 10-locking-system             | 9          | Distributed locking implementation      |
| 11-fulltext-search-redisearch | 10         | Full-text search with RediSearch        |
| 12-stream-pipeline            | 11         | Stream processing with consumer groups  |

## Usage Example

In your Python code, connect to the specific database:

```python
import redis

# Connect to Redis with specific database number
r = redis.Redis(host='localhost', port=6379, db=5)  # For 06-likes-system
```

## Running the Environment

Start the Redis container:
```
docker-compose up -d
```

Connect to Redis CLI:
```
docker exec -it redis-practice redis-cli
```

Switch to a specific database (example: db 5):
```
SELECT 5
```