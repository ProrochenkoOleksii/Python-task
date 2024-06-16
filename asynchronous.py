# Create 3 asynchronous functions: task1(), task2(), and task3().
# Each of these functions must have an asynchronous delay, such as with
# asyncio.sleep().
# Create an asynchronous main() function that calls these three functions.
# Run this main function and observe the order of tasks.

# In the comments to the code, specify the order in which the asynchronous tasks are called.
# Try different combinations of function calls in main() to see if
# how the execution order changes.
# Note the difference between asynchronous and synchronous code execution.

import asyncio
import random

async def task1():
    print("Початок виконання функції 1...")
    res=1
    for i in range (1,1000000):
        res = res+i*2
    await asyncio.sleep(2)  # Це асинхронна затримка
    print("Функція 1 завершила виконання!")

async def task2():
    print("Початок виконання функції 2...")
    my_list=[random.randint(1,1000000) for n in range(100000)]
    await asyncio.sleep(2)  # Це асинхронна затримка
    print("Функція 2 завершила виконання!")

async def task3():
    print("Початок виконання функції 3...")
    my_list_new=[random.randint(1,1000000) for n in range(900000)]
    my_list_new.sort()
    await asyncio.sleep(2)  # Це асинхронна затримка
    print("Функція 3 завершила виконання!")

async def main():
    await asyncio.gather(
        task2(),
        task3(),
        task1()
    )

asyncio.run(main()) #functions are wound in the order specified in main
