import asyncio


async def say_hi_dalay():
    print("Hi_1!")
    await asyncio.sleep(2)
    print("You are still in hi 1 here !")


async def say_hi_dalay2():
    print("Hi_2!")
    await asyncio.sleep(200)
    print("You are still in hi 2 here !")


async def main():
    # await say_hi_dalay()
    # await say_hi_dalay2()

    await asyncio.gather(say_hi_dalay(), say_hi_dalay2())

    print("Concluded!")


if __name__ == "__main__":
    asyncio.run(main())

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(say_hi_dalay())
    # oop = asyncio.get_event_loop()
    # oop.run_until_complete(say_hi_dalay2())
    # loop.close()
    # oop.close()
