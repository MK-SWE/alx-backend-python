#!/usr/bin/env python3
"""
Calculate the runtime of the function
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Test the runtime"""
    start = time.time()
    await async_comprehension()
    end = time.time()
    return (end - start)