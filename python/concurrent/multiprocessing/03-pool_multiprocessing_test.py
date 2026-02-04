import multiprocessing
import time

def math_numbers(value):
    result = value * 2
    time.sleep(5)
    print(f"Mathing {value} * 2 = {result} in the process {multiprocessing.current_process().name}")
    return result


def print_process_name():
    print("Starting process with name:", multiprocessing.current_process().name)


def main():
    
    pool_size = multiprocessing.cpu_count()

    print("Pool size:", pool_size)

    pool = multiprocessing.Pool(processes=pool_size, initializer=print_process_name)

    entry_values = list(range(1000))

    print("starting execution")
    results = pool.map(math_numbers, entry_values)

    # print("Results:", results)
    pool.close()
    pool.join()
    
    print("finishing execution")


if __name__=="__main__":
    main()