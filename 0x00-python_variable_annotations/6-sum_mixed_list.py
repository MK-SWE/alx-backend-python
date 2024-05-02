#!/usr/bin/env python3
"""
  return the sum of mixed datatype
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    return the sum as float
    """
    return sum(mxd_lst)
