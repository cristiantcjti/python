import multiprocessing
import time
import ctypes


def math_numbers_1(value, status):
    if status.value:
        result = value.value + 20
        status.value = False
    else:
        result = value.value + 40
        value.value = 400
        status.value = True

    print(f"Mathing 1 result {result}")
    time.sleep(0.01)

def math_numbers_2(value, status):
    if status.value:
        result = value.value + 40
        status.value = False
    else:
        result = value.value + 80
        value.value = 800
        status.value = True

    print(f"Mathing 2 result {result}")
    time.sleep(0.01)    

def main():
    value = multiprocessing.Value('i', 100)
    status = multiprocessing.Value(ctypes.c_bool, False)

    p1 = multiprocessing.Process(target=math_numbers_1, args=(value, status))
    p2 = multiprocessing.Process(target=math_numbers_2, args=(value, status))

    p1.start() 
    p2.start()

    p1.join()
    p2.join()

if __name__=="__main__":
    main()
    