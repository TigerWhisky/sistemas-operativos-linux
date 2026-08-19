import os,stat,tempfile
def describe_mode(mode): return stat.filemode(mode)
def main():
    with tempfile.NamedTemporaryFile(prefix='os-lab-',delete=False) as f: path=f.name; f.write(b'laboratory\n')
    try:
        st=os.stat(path); print('Path:',path); print('Mode:',describe_mode(st.st_mode)); print('Owner UID:',st.st_uid); print('Group GID:',st.st_gid)
    finally: os.unlink(path)
if __name__=='__main__': main()
