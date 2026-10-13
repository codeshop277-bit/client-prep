from pathlib import Path
import time
import asyncio
from typing import List

# with Path("data.txt").open("r") as file:
#     data = file.read()
#     print([line.strip() for line in data.splitlines()])
def print_name(name: str)  -> str:
    # time.sleep(2)
    print(f"Hello, {name}!")
    return name
a= print_name("Alice")
b= print_name("Bob")

# print(a, b)

async def print_name_async(name: str) -> str:
    # await asyncio.sleep(2)
    print(f"Hello, {name}!")
    return name

async def main():
    results = await asyncio.gather(
        print_name_async("Async-Alice"),  
        print_name_async("Async-Bob")
    )

    print(results)

asyncio.run(main())

async def run_search(name: str, delaay: int) -> List[dict]:
    await asyncio.sleep(delaay)
    return [{"name": name, "delay": delaay}]

async def run_multiple_searches():
    results = await asyncio.gather(
        run_search("Search1", 2),
        run_search("Search2", 3),
        run_search("Search3", 1)
    )
    for result in results:
        print(result)
    return results

# asyncio.run(run_multiple_searches())

def squared(n):
    for n in range(n):
        yield n*n

squares = squared(5)
for square in squares:
    print(square)

squaring = [number * number for number in range(5)]
print(squaring)
# print(next(squaring))

def read_non_empty_line(filepath):
    with open(filepath, "r")  as file:
        for line in file:
            line = line.strip()
            if line:
                yield line
read_non_empty_line('data.txt')