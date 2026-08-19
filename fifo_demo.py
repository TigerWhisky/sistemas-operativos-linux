import os,sys
FIFO=f'/tmp/fdlinux_fifo_{os.getuid()}'
def ensure():
    if not os.path.exists(FIFO): os.mkfifo(FIFO,0o600)
def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('read','write'): raise SystemExit('Uso: fifo_demo.py [read|write]')
    ensure()
    if sys.argv[1]=='read':
        print('A aguardar...');
        with open(FIFO) as f: print('Recebido:',f.readline().rstrip())
    else:
        with open(FIFO,'w') as f: f.write(f'Mensagem do processo {os.getpid()}\n')
    try: os.unlink(FIFO)
    except FileNotFoundError: pass
if __name__=='__main__': main()
