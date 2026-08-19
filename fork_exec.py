import os, sys

def main():
    print(f"Parent PID: {os.getpid()}")
    pid=os.fork()
    if pid==0:
        print(f"[child] PID={os.getpid()} PPID={os.getppid()}")
        os.execlp("python3","python3","-c","import os; print('[child exec] PID=',os.getpid())")
    os.waitpid(pid,0)
    print(f"[parent] child {pid} finished")

if __name__=='__main__':
    if not hasattr(os,'fork'): sys.exit('Linux/Unix required')
    main()
