#!/usr/bin/env python3
"""
  Execute multiple coroutines in the same time
"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Create the async functions and return list of float"""
    res = []
    lst = []
    for i in range(0, n):
        task = wait_random(max_delay)
        lst.append(task)
    for tasks in asyncio.as_completed((lst)):
        delay = await tasks
        res.append(delay)
    return res
