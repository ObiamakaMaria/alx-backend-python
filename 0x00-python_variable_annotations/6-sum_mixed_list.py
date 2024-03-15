#!/usr/bin/env python3
"""
The type-annotated function sum_mixed_list takes a list mxd_lst
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of the list as a float
    """
    return sum(mxd_lst)
