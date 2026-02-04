

# import asyncio
# from datetime import datetime
# import math


# def main():
#     print("Performing math process asynchronously...")

#     el = asyncio.get_event_loop()
    
#     el.run_until_complete(math_process(start=1, end=50000000))

#     start = datetime.now()

#     task_1 = el.create_task(math_process(start=1, end=10000000))
#     task_2 = el.create_task(math_process(start=10000001, end=20000000))
#     task_3 = el.create_task(math_process(start=20000001, end=30000000))
#     task_4 = el.create_task(math_process(start=30000001, end=40000000))
#     task_5 = el.create_task(math_process(start=40000001, end=50000000))
#     tasks = [task_1, task_2, task_3, task_4, task_5]    
    
#     tasks = asyncio.gather(*tasks)

#     el.run_until_complete(tasks)

#     time_taken = datetime.now() - start
    
#     print(f"Time taken: {time_taken.total_seconds()} seconds")


# async def math_process(start, end):
#     pos = start 
#     factor = 1000 * 1000
#     while pos < end:
#         pos += 1
#         math.sqrt((pos - factor) * (pos - factor))
    

# if __name__ == '__main__':
#     asyncio.run(main())

# Assinchrounously time: 9.25... seconds


"=================================="


import asyncio
from datetime import datetime
import math



# async def main(): 
#     print("Performing math process asynchronously...")

#     start = datetime.now()

    
#     await math_process(start=1, end=10000000),
#     await math_process(start=10000001, end=20000000),
#     await math_process(start=20000001, end=30000000),
#     await math_process(start=30000001, end=40000000),
#     await math_process(start=40000001, end=50000000)

#     time_taken = datetime.now() - start
    
#     print(f"Time taken: {time_taken.total_seconds()} seconds")



async def main(): 
    print("Performing math process asynchronously...")

    start = datetime.now()

    tasks = [
        math_process(start=1, end=10000000),
        math_process(start=10000001, end=20000000),
        math_process(start=20000001, end=30000000),
        math_process(start=30000001, end=40000000),
        math_process(start=40000001, end=50000000)
    ]
    
    await asyncio.gather(*tasks)

    time_taken = datetime.now() - start
    
    print(f"Time taken: {time_taken.total_seconds()} seconds")


async def math_process(start, end):
    pos = start 
    factor = 1000 * 1000
    while pos < end:
        pos += 1
        math.sqrt((pos - factor) * (pos - factor))
    

if __name__ == '__main__':
    asyncio.run(main()) 
    
