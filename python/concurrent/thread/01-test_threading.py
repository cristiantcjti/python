# import threading
import time

# def do_something(value):
#     print("Doing something with value:", value)
#     time.sleep(value)
#     print("Finishing something")  

# def do_something_else(value):
#     print("Doing something else with value:", value)    
#     time.sleep(10)
#     print("Finishing something else")  


# def cpu_intensive(n):
#     # This will run on single core due to GIL
#     result = 0
#     for i in range(n * 1000000):
#         result += i * i
#     print(f"CPU work done: {result}")


# def main():
#     th_1 = threading.Thread(target=cpu_intensive, args=(100,))
#     th_2 = threading.Thread(target=cpu_intensive, args=(100,))
    
#     print("starting execution")
#     start_time = time.time()
#     th_1.start()
#     th_2.start()
#     th_1.join()
#     th_2.join()
#     end_time = time.time()
#     print(f"finishing execution - Total time: {end_time - start_time:.2f}s")


# if __name__=="__main__":
#     main()


import threading

def busy_work(seconds):
    print(f"Starting work for {seconds} seconds")
    
    # Simple busy loop that holds the GIL
    count = 0
    target = seconds * 10_000_000  # Adjust multiplier as needed
    
    while count < target:
        count += 1
    
    print(f"Finished work: {count}")

def main():
    th_1 = threading.Thread(target=busy_work, args=(3,))
    th_2 = threading.Thread(target=busy_work, args=(3,))
    
    print("starting execution")
    start_time = time.time()
    th_1.start()
    th_2.start()
    th_1.join()
    th_2.join()
    end_time = time.time()
    print(f"finishing execution - Total time: {end_time - start_time:.2f}s")


if __name__=="__main__":
    main()