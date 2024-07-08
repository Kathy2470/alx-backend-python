#!/usr/bin/env python3

"""
This module provides a function to create an asyncio.Task for
wait_random coroutine.
"""

import asyncio
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random coroutine with
    the given max_delay.

    Args:
        max_delay (int): Maximum delay value for wait_random coroutine.

    Returns:
        asyncio.Task: Task object wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    # Example usage as in 3-main.py
    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
