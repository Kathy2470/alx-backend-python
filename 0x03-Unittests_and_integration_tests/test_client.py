#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for GithubOrgClient.
    """

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    @patch('client.GithubOrgClient.get_repo_info')  # Assuming this method provides repo information
    def test_has_license(self, repo, license_key, expected, mock_get_repo_info):
        """
        Test has_license method with various repo licenses and license_key.
        """
        # Set the mock to return the repo dictionary
        mock_get_repo_info.return_value = repo
        
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call the has_license method
        result = client.has_license(license_key)
        
        # Assert the result
        self.assertEqual(result, expected)

        # Ensure that get_repo_info was called exactly once
        mock_get_repo_info.assert_called_once()

if __name__ == '__main__':
    unittest.main()
