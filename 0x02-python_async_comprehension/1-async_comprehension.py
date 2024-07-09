#!/usr/bin/env python3
"""
This module provides a coroutine that collects 10 random numbers using
an async comprehension over async_generator and returns the 10 random numbers.
"""

import asyncio
from typing import List
from async_generator import async_generator
from importlib import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Asynchronously creates a list of 10 numbers from a generator.
    '''
    return [num async for num in async_generator()]
