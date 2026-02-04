import asyncio

async def say_hi():
    print('Hi!')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(say_hi())
    loop.close()
    #asyncio.run(say_hi())