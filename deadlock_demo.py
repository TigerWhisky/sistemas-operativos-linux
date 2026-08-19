import threading,time
a=threading.Lock(); b=threading.Lock()
def A():
    with a: print('A acquired A',flush=True); time.sleep(.2); print('A waiting B',flush=True); b.acquire()
def B():
    with b: print('B acquired B',flush=True); time.sleep(.2); print('B waiting A',flush=True); a.acquire()
if __name__=='__main__':
    x=threading.Thread(target=A); y=threading.Thread(target=B); x.start(); y.start(); x.join(); y.join()
