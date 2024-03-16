#!/usr/bin/env python3
"""
Async Generator: Generates random numbers asynchronously.
"""

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers.
    """
    for _ in range(10):
        random_number = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield random_number
