#!/usr/bin/env python3
"""
  sum_list  a function that return the sum of a given list
"""


def sum_list(list: list[float]) -> float:
    """ Return the list sum"""
    res = 0
    for i in list:
        res += i
    return res
