import aioredis

async def get_redis():
    redis = await aioredis.create_redis_pool(os.getenv("REDIS_URL"))
    try:
        yield redis
    finally:
        redis.close()
        await redis.wait_closed()