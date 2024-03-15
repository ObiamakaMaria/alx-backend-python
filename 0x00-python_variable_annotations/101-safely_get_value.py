#!/usr/bin/env python3
"""
Duck typing the first element of a sequence
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] =
                     None) -> Union[Any, T]:
    """
    Returns the  first element of a sequence
    """
    if key in dct:
        return dct[key]
    else:
        return default
