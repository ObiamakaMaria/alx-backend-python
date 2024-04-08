#!/usr/bin/env python3
"""Unit tests for the client functionality"""


import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
GithubOrgClient = __import__("client").GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''Test suite for the GithubOrgClient class'''

    @parameterized.expand([('google'), ('abc')])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_org):
        '''Test fetching different organizations'''
        test_org = GithubOrgClient(org)
        res = test_org.org
        self.assertEqual(res, mock_org.return_value)
        mock_org.assert_called_once()
