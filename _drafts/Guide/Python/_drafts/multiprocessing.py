import time
from datetime import datetime
from multiprocessing import Process


def f():
    amount = 1
    now = datetime.now()
    print(f'{now}. Sleeping for {amount} sec(s).')
    time.sleep(amount)
    print(f'{now}. Done sleeping...')


if __name__ == '__main__':
    process = []
    for _ in range(10):
        p = Process(target=f)
        p.start()
        process.append(p)

    for p in process:
        p.join()

    for _ in range(10):
        f()