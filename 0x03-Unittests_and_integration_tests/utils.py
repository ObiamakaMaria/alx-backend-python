#!/usr/bin/env python3
"""General utilities for GitHub organization client."""

import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access a nested map using a path of keys.
    
    Parameters
    ----------
    nested_map: Mapping
        A nested map.
    path: Sequence
        A sequence of keys representing a path to the value.
    
    Example
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


def get_json(url: str) -> Dict:
    """Fetch JSON from a remote URL."""
    response = requests.get(url)
    return response.json()
