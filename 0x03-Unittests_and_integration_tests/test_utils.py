#!/usr/bin/env python3
"""
Unit tests for utils.memoize.
"""

import unittest
from unittest.mock import patch
from utils import memoize

class TestMemoize(unittest.TestCase):
    """
    Test class for the memoize decorator.
    """

    def test_memoize(self):
        """
        Test memoize decorator to ensure it caches results.
        """
        class TestClass:
            def a_method(self):
                """
                Method that returns a constant value.
                """
                return 42

            @memoize
            def a_property(self):
                """
                Property that uses the memoize decorator to cache results.
                """
                return self.a_method()

        # Create an instance of TestClass
        obj = TestClass()

        # Mock a_method
        with patch.object(obj, 'a_method', return_value=42) as mock_a_method:
            # Call the memoized method twice
            result1 = obj.a_property()
            result2 = obj.a_property()

            # Verify that a_method was only called once
            mock_a_method.assert_called_once()

            # Verify that the result of both calls to a_property is the same
            self.assertEqual(result1, result2)
            self.assertEqual(result1, 42)

if __name__ == '__main__':
    unittest.main()
