#!/usr/bin/env python3
"""
This module provides a function to create an asyncio Task that waits
for a random delay.
"""

from asyncio import create_task
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task that waits for a random delay.

    Args:
        max_delay (int): Maximum delay value.

    Returns:
        asyncio.Task: A task that waits for a random delay.
    """
    return create_task(wait_random(max_delay))
