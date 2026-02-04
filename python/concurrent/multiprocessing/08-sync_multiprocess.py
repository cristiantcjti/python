import multiprocessing

def deposit(balance, lock):
    for _ in range(10000):
        with lock:
            balance.value += 1

def withdraw(balance, lock):
    for _ in range(10000):
        with lock:
            balance.value -= 1

def main(balance, lock):
    pc1 = multiprocessing.Process(target=deposit, args=(balance, lock))
    pc2 = multiprocessing.Process(target=withdraw, args=(balance, lock))

    pc1.start()
    pc2.start() 

    pc1.join()
    pc2.join()

if __name__=="__main__":
    balance = multiprocessing.Value('i', 200)

    lock = multiprocessing.RLock()
    
    print("Initial balance: ", balance.value)

    for _ in range(10):
        main(balance, lock)

    print("Final balance: ", balance.value)