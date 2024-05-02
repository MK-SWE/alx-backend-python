#!/usr/bin/env python3
"""
make_multiplier that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier
"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> float:
    """
    return multiplier a function
    """
    def mult(n: float) -> float:
        """ multiplies a float by multiplier """
        return float(n * multiplier)
    return mult
