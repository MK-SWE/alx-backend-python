#!/usr/bin/env python3
"""
  Execute multiple coroutines in the same time
"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List



def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

async def wait_n(n: int, max_delay: int) -> List[float]:
    lst = []
    for i in range(0, n):
        delay = await wait_random(max_delay)
        lst.append(delay)
    res = merge_sort(lst)
    return res
