#!/usr/bin/env python3
'''Implementation of async programming in python'''


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''This is an async function'''
    listed = []
    for _ in range(n):
        value = asyncio.create_task(wait_random(max_delay))
        listed.append(value)
    res = [await r for r in asyncio.as_completed(listed)]
    return res
