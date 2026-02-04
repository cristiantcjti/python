import asyncio
import aiofiles


async def exemple_aiofiles_1():
    async with aiofiles.open('16_text.txt') as file:
        content = await file.read()
    print("Content:", content)
    print("###### End Content #######")


async def exemple_aiofiles_2():
    async with aiofiles.open('16_text.txt') as file:
        async for line in file:
            print("Lines:", line)
    
    print('File written successfully!')

def main():
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(exemple_aiofiles_1())
    # loop.run_until_complete(exemple_aiofiles_2())
    
    asyncio.run(exemple_aiofiles_1())
    asyncio.run(exemple_aiofiles_2())

if __name__ == '__main__':
    main()