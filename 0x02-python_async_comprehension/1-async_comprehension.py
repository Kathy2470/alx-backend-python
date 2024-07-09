#!/usr/bin/env python3
"""
This module provides a coroutine that collects 10 random numbers using
an async comprehension over async_generator and returns the 10 random numbers.
"""

import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects 10 random numbers from async_generator.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    numbers: List[float] = [num async for num in async_generator()]
    return numbers
