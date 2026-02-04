import multiprocessing


def ping(conn):
    print("ping sending message")
    conn.send("Python ")
    print("ping sent message")

def pong(conn):
    print("pong waiting message")
    msg = conn.recv()
    print("pong received message")
    print(f"Message is: {msg}, is awesome!")

def main():
    conn1, conn2 = multiprocessing.Pipe(True)

    p1= multiprocessing.Process(target=ping, args=(conn1,))
    p2= multiprocessing.Process(target=pong, args=(conn2,))
    # p2.start()
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__=="__main__":
    main()