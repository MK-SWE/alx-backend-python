#!/usr/bin/env python3
"""
  Duck typing - first element of a sequence
"""
from typing import List, Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """ Return a zoomed array"""
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
