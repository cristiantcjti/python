import multiprocessing

print("Starting process with name:", multiprocessing.current_process().name)

def do_something(value):
    print("Doing something with value:", value)


def main():
    
    th = multiprocessing.Process(target=do_something, args=("python",), name="Process inside main")
    
    print("starting execution")
    th.start()

    th.join()
    print("finishing execution")


if __name__=="__main__":
    main()
