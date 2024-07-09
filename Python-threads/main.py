from multiprocessing import Process
from threading import Thread

import os
import time


def square_numbers():
    for i in range(1000):
        i * i
        time.sleep(0.1)



processes = []
num_processes = os.cpu_count()

# create proceses
for i in range(0, num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

for p in processes:
    p.start()

for p in processes:
    p.join()

print('end main')


threads = []
num_threads = 10


# create threads
for i in range(0, num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
