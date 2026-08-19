from queue import Queue
from threading import Thread
import time
SENTINEL=object()
def producer(q,count=10):
    for i in range(count): q.put(i); print('producer ->',i); time.sleep(.02)
    q.put(SENTINEL)
def consumer(q):
    while True:
        x=q.get()
        try:
            if x is SENTINEL: return
            print('consumer <-',x); time.sleep(.03)
        finally: q.task_done()
def main():
    q=Queue(maxsize=3); a=Thread(target=producer,args=(q,)); b=Thread(target=consumer,args=(q,)); a.start(); b.start(); a.join(); q.join(); b.join()
if __name__=='__main__': main()
