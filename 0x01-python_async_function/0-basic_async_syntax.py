#!/usr/bin/env python3
'''An asynchronous coroutine implementation '''


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This asynchronous coroutine  wait_random takes in an integer 
    """
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
