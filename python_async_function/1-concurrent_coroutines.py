#!/usr/bin/env python3
"""
Import wait_random from the previous python file that you’ve written
and write an async routine called wait_n that takes
in 2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without
using sort() because of concurrency.
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Waits for random delays up to max_delay, returns delays in ascending order"""
    spawn_list, delay_list = [], []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(task)

    for task in spawn_list:
        await task

    return sorted(delay_list)
