#!/usr/bin/env python3
"""
TestGithubOrgClient module
"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class
    """
    @patch('client.GithubOrgClient._GithubOrgClient__get_org')
    def test_public_repos_url(self, mock_get_org):
        """
        Test that _public_repos_url returns the expected URL
        """
        mock_get_org.return_value = {'login': 'test-org'}
        client = GithubOrgClient('test-org')
        expected_url = 'https://api.github.com/orgs/test-org/repos'
        self.assertEqual(client._public_repos_url, expected_url)

if __name__ == '__main__':
    unittest.main()
