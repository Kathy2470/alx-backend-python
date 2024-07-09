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
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator and returns the 10 random numbers.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator()]

if __name__ == "__main__":
    async def main() -> None:
        """
        Collects and prints the values returned by the async_comprehension coroutine.
        """
        result = await async_comprehension()
        print(result)

    asyncio.run(main())
