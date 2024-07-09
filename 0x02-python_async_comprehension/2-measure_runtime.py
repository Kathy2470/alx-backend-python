#!/usr/bin/env python3
"""
This module provides a coroutine that measures the total runtime
of executing async_comprehension four times in parallel using asyncio.gather.
"""

import asyncio
from typing import List
from time import perf_counter
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = perf_counter()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end_time = perf_counter()
    total_runtime = end_time - start_time

    return total_runtime

if __name__ == "__main__":
    async def main() -> None:
        """
        Runs measure_runtime and prints the total runtime.
        """
        runtime = await measure_runtime()
        print(f"Total runtime: {runtime} seconds")

    asyncio.run(main())
