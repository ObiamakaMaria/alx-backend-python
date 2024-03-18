#!/usr/bin/env python3
'''Impplementation of async programming in python'''


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''An async function'''
    return asyncio.create_task(wait_random(max_delay))
