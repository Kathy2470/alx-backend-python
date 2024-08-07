#!/usr/bin/env python3

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, T],
    key: Any,
    default: Union[T, None] = None
) -> Union[T, Any]:
    if key in dct:
        return dct[key]
    else:
        return default
