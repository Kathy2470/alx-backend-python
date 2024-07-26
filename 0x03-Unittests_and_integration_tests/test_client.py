#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, MagicMock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for GithubOrgClient.
    """

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test public_repos method with mocked _public_repos_url and get_json.
        """
        # Define the mock payload for get_json
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = mock_payload

        # Mock _public_repos_url to return a test URL
        with patch('client.GithubOrgClient._public_repos_url', new_callable=property) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/test/repos"
            
            # Create an instance of GithubOrgClient
            client = GithubOrgClient("test_org")

            # Call the public_repos method
            repos = client.public_repos()

            # Define the expected repos list
            expected_repos = mock_payload

            # Test that the list of repos is what you expect
            self.assertEqual(repos, expected_repos)

            # Test that _public_repos_url and get_json were called once
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/test/repos")

if __name__ == '__main__':
    unittest.main()
