import time

# from concurrent.futures import ThreadPoolExecutor as Executor 
from concurrent.futures import ProcessPoolExecutor as Executor

def run():
    print('[', end='', flush=True)
    for _ in range(1, 11):
        print('#', end='', flush=True)
        time.sleep(0.5)
    print(']', end='', flush=True)

    return "Done"

if __name__=="__main__":
    with Executor() as executor:
        future = executor.submit(run)

    print(future.result())