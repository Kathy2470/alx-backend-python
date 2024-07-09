#!/usr/bin/env python3
"""
This module provides an asynchronous generator coroutine
that yields a random number between 0 and 10, 10 times,
each time asynchronously waiting for 1 second.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields a random number between 0 and 10, 10 times,
    each time asynchronously waiting for 1 second.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
