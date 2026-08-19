import signal,time
running=True
def handler(signum,frame):
    global running; print(f'\nReceived signal {signum}'); running=False
def main():
    signal.signal(signal.SIGINT,handler); print('Running. Press Ctrl+C.')
    while running: time.sleep(.5)
    print('Clean shutdown.')
if __name__=='__main__': main()
