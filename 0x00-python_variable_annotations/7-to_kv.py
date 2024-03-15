#!/usr/bin/env python3
"""
The type-annotated function to_kv takes a string k and an int OR float v
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of k and the square of v
    """
    return (k, v * v)
