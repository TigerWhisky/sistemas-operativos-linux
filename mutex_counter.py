import threading
ITERATIONS=100_000; THREADS=4
def run_once():
    counter=0; lock=threading.Lock()
    def inc():
        nonlocal counter
        for _ in range(ITERATIONS):
            with lock: counter+=1
    ws=[threading.Thread(target=inc) for _ in range(THREADS)]
    [w.start() for w in ws]; [w.join() for w in ws]
    return counter
if __name__=='__main__': print(run_once())
