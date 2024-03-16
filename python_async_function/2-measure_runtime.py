#!/usr/bin/env python3
"""
Measures the runtime of async functions.
"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the runtime of the async function wait_n."""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - start_time) / n
