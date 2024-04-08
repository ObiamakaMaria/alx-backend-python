#!/usr/bin/env python3
"""Unit tests for utility functions"""


import unittest
from unittest.mock import patch
from parameterized import parameterized  # type: ignore
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json
memoize = __import__("utils").memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for accessing nested maps"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, result: int) -> None:
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        '''Test exception handling for access_nested_map function'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test cases for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, req):
        """Test get_json function"""
        req.return_value.json.return_value = test_payload
        response = get_json(test_url)
        self.assertEqual(response, test_payload)
        req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test cases for memoize function"""

    def test_memoize(self):
        """Test memoization"""
        class TestClass:
            """Test class"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock.assert_called_once()
