import threading
ITERATIONS=100_000; THREADS=4
def run_once():
    counter=0
    def inc():
        nonlocal counter
        for _ in range(ITERATIONS):
            current=counter; counter=current+1
    ws=[threading.Thread(target=inc) for _ in range(THREADS)]
    [w.start() for w in ws]; [w.join() for w in ws]
    return counter
if __name__=='__main__':
    expected=ITERATIONS*THREADS
    print('Expected:',expected)
    for i in range(5): print('Run',i+1,run_once())
