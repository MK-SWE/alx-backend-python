#!/usr/bin/env python3
"""
  return a list of values
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a list of values"""
    return [(i, len(i)) for i in lst]
