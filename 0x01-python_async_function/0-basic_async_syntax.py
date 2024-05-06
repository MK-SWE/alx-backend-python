#!/usr/bin/env python3
"""
  The First Async function
"""
import random


async def wait_random(max_delay=10):
    """ Return a random value between zero and max_delay"""
    res = random.uniform(0, max_delay)
    return res
