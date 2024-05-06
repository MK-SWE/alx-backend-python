#!/usr/bin/env python3
"""
  The First Async function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Return a random value between zero and max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
