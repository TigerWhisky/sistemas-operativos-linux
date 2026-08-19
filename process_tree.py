import os,time

def main():
    print(f"root PID={os.getpid()}",flush=True)
    pids=[]
    for label in ('child-A','child-B'):
        pid=os.fork()
        if pid==0:
            print(f"{label}: PID={os.getpid()} PPID={os.getppid()}",flush=True); time.sleep(3); os._exit(0)
        pids.append(pid)
    for pid in pids: os.waitpid(pid,0)
    print('children finished')
if __name__=='__main__': main()
