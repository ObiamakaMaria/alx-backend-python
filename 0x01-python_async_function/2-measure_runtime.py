#!/usr/bin/env python3
'''Implemetation of  async programming  in python'''


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''This async function measures function's time'''
    starter = time.perf_counter()
    asyncio.run((wait_n(n, max_delay)))
    end = time.perf_counter() - starter
    return end / n
