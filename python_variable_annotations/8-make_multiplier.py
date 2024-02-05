#!/usr/bin/env python3
"""
8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    this is a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies a float
    by multiplier.
    """
    def multiplier_function(m: float) -> float:
        return m * multiplier
    return multiplier_function
