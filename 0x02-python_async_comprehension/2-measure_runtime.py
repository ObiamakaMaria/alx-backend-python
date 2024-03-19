#!/usr/bin/env python3
''' An implementation of asynchronous programming as in PEP 525'''


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''The asynchronous generator function'''
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.perf_counter() - start
    return (end)