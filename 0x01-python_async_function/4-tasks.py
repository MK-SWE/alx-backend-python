#!/usr/bin/env python3
"""
  Execute multiple coroutines in the same time
"""
import asyncio
from typing import List
task_wait_random  = __import__('3-tasks').task_wait_random 


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Create the async functions and return list of float"""
    res = []
    lst = []
    for i in range(0, n):
        task = task_wait_random(max_delay)
        lst.append(task)
    for tasks in asyncio.as_completed((lst)):
        delay = await tasks
        res.append(delay)
    return res
