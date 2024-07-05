#!/usr/bin/env python3
'''Module for calculating the length of each element in a list'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list of tuples, where each tuple contains an element
    from the input list and its length'''
    return [(i, len(i)) for i in lst]
