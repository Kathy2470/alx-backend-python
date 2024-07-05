#!/usr/bin/env python3
'''Module for creating a tuple from a string and a number'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns a tuple with the string k and the square of the number v'''
    return k, v ** 2
