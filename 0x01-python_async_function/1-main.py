#!/usr/bin/env python3
'''
Test file for printing the correct output of the measure_time coroutine
'''

import asyncio

measure_time = __import__('2-measure_time').measure_time

async def main():
    n = 5
    max_delay = 9
    elapsed_time = await measure_time(n, max_delay)
    print("Approximate elapsed time falls within an acceptable range: {}.".format(0 <= elapsed_time <= max_delay * 1.02))

if __name__ == "__main__":
    asyncio.run(main())
