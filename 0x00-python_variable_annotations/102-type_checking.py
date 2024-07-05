#!/usr/bin/env python3
from typing import Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    Zooms in on an array by a specified factor.

    Args:
        lst (Tuple): The input array.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        Tuple: The zoomed-in array.
    """
    zoomed_in: Tuple = tuple(
        item for item in lst
        for _ in range(factor)
    )
    return zoomed_in


array: Tuple = (12, 72, 91)


zoom_2x: Tuple = zoom_array(array)
print("Zoomed 2x:", zoom_2x)


zoom_3x: Tuple = zoom_array(array, 3)
print("Zoomed 3x:", zoom_3x)
