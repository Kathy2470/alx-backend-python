#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for GithubOrgClient.
    """

    @parameterized.expand([
        ("google", {"org": "google"}),
        ("abc", {"org": "abc"}),
    ])
    @patch('client.get_json')  # Mock the get_json method in the client module
    def test_org(self, org_name, expected_payload, mock_get_json):
        """
        Test GithubOrgClient.org returns the correct value.
        """
        # Set up the mock return value for get_json
        mock_get_json.return_value = expected_payload
        
        # Create an instance of GithubOrgClient with the parameterized org_name
        client = GithubOrgClient(org_name)
        
        # Call the org property
        result = client.org
        
        # Assert that get_json was called once with the expected argument
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')
        
        # Assert that the org property returns the correct value
        self.assertEqual(result, expected_payload)

if __name__ == '__main__':
    unittest.main()
