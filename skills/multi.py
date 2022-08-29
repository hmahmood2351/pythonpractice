#separate processes and separate threads (although due to GIL only one thread at a time)

#multiprocessing

from asyncio import threads
from concurrent.futures import thread
from multiprocessing import Process
import os 
import time
from threading import Thread

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []
num_threads = os.cpu_count()

# create processes 

for i in range(num_threads):
    t = Thread(target=square_numbers())
    thread.append(t)


for p in threads:
    p.start()

for p in threads:
    p.join()

print('End main')
