#!/usr/bin/env python3
"""
The type-annotated function sum_list takes list input_list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of the list of floats
    """
    return sum(input_list)
