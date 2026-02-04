import datetime
import asyncio

async def generate_data(quantity: int, data: asyncio.Queue):
    print(f"Generating {quantity} data...")
    for index in range(1, quantity + 1):
        item = index * index
        await data.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.00001)
    print(f"Generated {quantity} data successfully!")


async def process_data(quantity: int, data: asyncio.Queue):
    print(f"Processing {quantity} data...")
    processed = 0
    while processed < quantity:
        data_to_process = await data.get()
        print(f"Processed data: {data_to_process}")
        processed += 1
        await asyncio.sleep(0.00001)
    print(f"Processed {quantity} data successfully!")


def main():
    total = 50
    data = asyncio.Queue()
    print("Generating and processing data")

    loop = asyncio.get_event_loop()
    task1 = loop.create_task(generate_data(total, data))
    task2 = loop.create_task(generate_data(total, data))
    task3 = loop.create_task(process_data(total * 2, data))
    task4 = loop.create_task(process_data(total * 2, data))

    tasks = asyncio.gather(task1, task2, task3, task4)
    loop.run_until_complete(tasks)


if __name__=='__main__':
    main()