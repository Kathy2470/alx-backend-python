#!/usr/bin/env python3

"""
This module provides a function to create asyncio.Tasks for wait_n coroutine.
"""

import asyncio
from basic_async_syntax import wait_random


async def task_wait_random(max_delay: int) -> float:
    """
    Coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): Maximum delay value.

    Returns:
        float: Random delay generated.
    """
    delay = await wait_random(max_delay)
    return delay


async def task_wait_n(n: int, max_delay: int) -> list:
    """
    Create asyncio.Tasks for wait_n coroutine with the given n and max_delay.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay value for each coroutine.

    Returns:
        list: List of float values representing the delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Example usage
    async def test_task_wait_n(n: int, max_delay: int) -> None:
        delays = await task_wait_n(n, max_delay)
        print(delays)

    asyncio.run(test_task_wait_n(5, 6))
