#!/usr/bin/env python3

"""
This module provides an asynchronous function to wait for a random delay
multiple times and return the delays in ascending order.
"""

import asyncio
import heapq
from typing import List
from basic_async_syntax import wait_random


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
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        heapq.heappush(delays, delay)

    return [heapq.heappop(delays) for _ in range(n)]
