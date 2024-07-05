#!/usr/bin/env python3
"""
This module contains a function to safely get a value from a dictionary.
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, T],
    key: Any,
    default: Union[T, None] = None
) -> Union[T, None]:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Mapping[Any, T]):
            The dictionary to get the value from.
        key (Any):
            The key to get the value for.
        default (Union[T, None], optional):
            The default value to return if the key is not found.
            Defaults to None.

    Returns:
        Union[T, None]:
            The value from the dictionary or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
