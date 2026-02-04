import datetime
from compute import do_compute

def main():
    start = datetime.datetime.now()

    do_compute(end=50000000)

    _time = datetime.datetime.now() - start

    print(f"Complete in {_time.total_seconds():.2f} seconds.")

if __name__ == "__main__":
    main()

"""
Complete in 9.99 seconds. 
"""