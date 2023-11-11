import asyncio
import requests




async def print_numbers(num):
    for i in range(1, num + 1):
        print(i)
        await asyncio.sleep(1)

async def main():
    num1 = 13
    num2 = 12

    task1 = asyncio.create_task(print_numbers(num1))
    task2 = asyncio.create_task(print_numbers(num2))

    await asyncio.gather(task1, task2)

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()