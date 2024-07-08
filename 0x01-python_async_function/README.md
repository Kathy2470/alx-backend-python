0x01. Python - Async

Python Async Functions and Tasks
This repository contains Python scripts demonstrating asynchronous programming using asyncio. Each script corresponds to a specific task focusing on coroutine execution, task creation, and measuring execution times.

Files and Descriptions
2-measure_runtime.py

Calculates the average execution time for a coroutine using asyncio.
Imports wait_n from another module and measures its execution time.
3-tasks.py

Defines a coroutine task_wait_random that waits for a random delay.
Implements a function task_wait_n to create multiple asyncio tasks using task_wait_random.
4-tasks.py

Refactors wait_n into task_wait_n where each task is created using task_wait_random.
Demonstrates how to run and print multiple asyncio tasks concurrently.
Usage
To execute any of the scripts:

bash
Copy code
python3 script_name.py
Replace script_name.py with the actual filename you wish to execute.

Requirements
Python 3.7 or higher
asyncio library
pycodestyle (for code style adherence)
Installation
No special installation is required beyond having Python 3.7+ and installing dependencies if needed (asyncio, pycodestyle).

Author
Kathylene
