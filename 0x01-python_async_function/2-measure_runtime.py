#!/usr/bin/env python3

"""
This module provides a function to measure the execution time of
wait_n coroutine and calculate the average time per coroutine.
"""

import asyncio
import time
from _1_concurrent_coroutines import wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay value for each coroutine.

    Returns:
        float: Average time taken per coroutine.
    """
    start_time = time.time()

    await wait_n(n, max_delay)

    end_time = time.time()
    total_time = end_time - start_time

    average_time = total_time / n
    return average_time


if __name__ == "__main__":
    # Example usage as in 2-main.py
    n = 5
    max_delay = 9
    print(asyncio.run(measure_time(n, max_delay)))
