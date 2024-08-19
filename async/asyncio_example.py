import asyncio


async def print1():
    print(1)


async def print2():
    await asyncio.sleep(10)
    print(2)


async def print3():
    print(3)


async def main():
    print1()
    print2()
    print2()


asyncio.run()
