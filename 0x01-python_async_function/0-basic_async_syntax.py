#!/usr/bin/env python3

"""
This module provides an asynchronous function to wait for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay (included) seconds
    and return it.

    Args:
    max_delay (int, optional): The maximum delay in seconds.
                               Defaults to 10.

    Returns:
    float: The random delay in seconds.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
