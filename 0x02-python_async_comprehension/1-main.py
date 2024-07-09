#!/usr/bin/env python3

import asyncio
from async_comprehension import async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main())
