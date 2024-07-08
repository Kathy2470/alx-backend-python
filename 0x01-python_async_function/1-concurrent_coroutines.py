#!/usr/bin/env python3

"""
This module provides an asynchronous function to wait for a random delay
multiple times.
"""

import asyncio
from typing import List

from.0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return the
    list of delays.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: The list of delays in ascending order.
    """

    tasks = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    delays = await asyncio.gather(*tasks)

    sorted_delays_task = asyncio.create_task(
        sort_delays(delays)
    )

    sorted_delays = await sorted_delays_task

    return sorted_delays


async def sort_delays(delays: List[float]) -> List[float]:
    """
    Sort the list of delays in ascending order using a merge sort algorithm.

    Args:
        delays (List[float]): The list of delays to sort.

    Returns:
        List[float]: The sorted list of delays.
    """

    if len(delays) <= 1:
        return delays

    mid = len(delays) // 2
    left_half = delays[:mid]
    right_half = delays[mid:]

    left_half_task = asyncio.create_task(
        sort_delays(left_half)
    )
    right_half_task = asyncio.create_task(
        sort_delays(right_half)
    )

    left_half = await left_half_task
    right_half = await right_half_task

    return merge(left_half, right_half)


def merge(left: List[float], right: List[float]) -> List[float]:
    """
    Merge two sorted lists into one sorted list.

    Args:
        left (List[float]): The first sorted list.
        right (List[float]): The second sorted list.

    Returns:
        List[float]: The merged sorted list.
    """

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged
