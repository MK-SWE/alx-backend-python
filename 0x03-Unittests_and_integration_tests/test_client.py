#!/usr/bin/env python3
"""
    Unittest for the clients
"""
import unittest
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import (
    GithubOrgClient
)



class TestGithubOrgClient(unittest.TestCase):
    """
        define unittest class for nested map
    """
    def test_org(self, data, path, expected_result):
        """start the unittest"""
        pass
