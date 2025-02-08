import os
import asyncio
import aioredis
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from app.utils.logging_config import logger
from app.services.performance_optimizer import PerformanceOptimizer
from app.services.load_tester import LoadTester
from app.services.system_monitor import SystemMonitor

load_dotenv()

app = FastAPI()

redis_client = None

@app.on_event("startup")
async def startup():
    global redis_client
    redis_client = await aioredis.from_url(os.getenv("REDIS_URL"))

    FastAPILimiter.init(redis_client)

    optimizer = PerformanceOptimizer()
    await optimizer.optimize_system_performance({
        'response_time': 0,
        'error_rate': 0
    })

    load_tester = LoadTester()
    await load_tester.run_load_test({
        'num_users': 100,
        'scenarios': {
            'create_order': 50,
            'search_drivers': 30,
            'update_location': 20
        }
    })

    asyncio.create_task(background_monitor_system_health())

@app.on_event("shutdown")
async def shutdown():
    await redis_client.close()

async def background_monitor_system_health():
    try:
        while True:
            monitor = SystemMonitor()
            metrics, alerts = await monitor.monitor_system_health()
            await store_system_metrics(metrics)

            optimizer = PerformanceOptimizer()
            await optimizer.handle_alerts(alerts)

            await asyncio.sleep(60)
    except Exception as e:
        logger.error(f"Error in background system monitoring: {e}")

async def store_system_metrics(metrics):
    try:
        new_metric = SystemMetric(
            response_time=metrics['application_metrics']['response_time'],
            cpu_usage=metrics['system_metrics']['cpu_usage'],
            memory_usage=metrics['system_metrics']['memory_usage'],
            error_rate=metrics['application_metrics']['error_rate'],
            active_users=await get_active_users_count(),
            pending_orders=await get_pending_orders_count(),
            timestamp=datetime.utcnow()
        )
        await new_metric.save()
        await db.session.commit()
    except Exception as e:
        await db.session.rollback()
        logger.error(f"Error storing system metrics: {e}")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)