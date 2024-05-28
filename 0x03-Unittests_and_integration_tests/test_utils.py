#!/usr/bin/env python3
"""
    Unittest for the utils
"""
import unittest
from parameterized import parameterized
from test_utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
        define unittest class for nested map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, data, path, expected_result):
        """start the unittest"""
        result = access_nested_map(data, path)
        self.assertEqual(result, expected_result)
