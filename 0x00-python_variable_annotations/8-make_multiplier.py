#!/usr/bin/env python3
"""
 The type-annotated function make_multiplier takes a float multiplier
 """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier
    """
    def multiply(num: float) -> float:
        return num * multiplier
    return multiply
