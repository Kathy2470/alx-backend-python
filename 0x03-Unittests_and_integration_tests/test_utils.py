#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map, utils.get_json, and utils.memoize.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map with various inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map raises KeyError for invalid paths.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(path[-1]))

class TestGetJson(unittest.TestCase):
    """
    Test class for get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json with various inputs.
        """
        # Create a mock response object with a json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Set the mock object to return the mock response
        mock_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Assert that requests.get was called exactly once with the test_url
        mock_get.assert_called_once_with(test_url)

        # Assert that the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """
    Test class for memoize decorator.
    """

    def test_memoize(self):
        """
        Test memoize decorator with a method call.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            instance = TestClass()
            # Call a_property twice
            result1 = instance.a_property
            result2 = instance.a_property

            # Assert that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Assert that a_method was called only once
            mock_method.assert_called_once()

if __name__ == '__main__':
    unittest.main()
