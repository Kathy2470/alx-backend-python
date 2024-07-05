#!/usr/bin/env python3
'''Module for safely returning the first element of a list'''

from typing import Sequence, Any, Union, Type


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns the first element of the input list
    if it's not empty, otherwise returns None'''
    if lst:
        return lst[0]
    else:
        return None
