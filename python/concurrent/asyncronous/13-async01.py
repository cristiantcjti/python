import datetime
import asyncio

async def generate_data(quantity: int, data: asyncio.Queue):
    print(f"Generating {quantity} data...")
    for index in range(1, quantity + 1):
        item = index * index
        await data.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.001)
    print(f"Generated {quantity} data successfully!")


async def process_data(quantity: int, data: asyncio.Queue):
    print(f"Processing {quantity} data...")
    processed = 0
    while processed < quantity:
        await data.get()
        processed += 1
        await asyncio.sleep(0.001)
    print(f"Processed {quantity} data successfully!")


if __name__=='__main__':
    total = 5000
    data = asyncio.Queue()
    loop = asyncio.get_event_loop()
    
    print("Generating and processing data")

    loop.run_until_complete(generate_data(total, data))
    loop.run_until_complete(generate_data(total, data))
    loop.run_until_complete(process_data(total * 2 , data))
    
    loop.close()