from pathlib import Path
def read_status():
    p=Path('/proc/self/status')
    if not p.exists(): raise RuntimeError('Linux /proc required')
    out={}
    for line in p.read_text().splitlines():
        if ':' in line: k,v=line.split(':',1); out[k.strip()]=v.strip()
    return out
def main():
    s=read_status()
    for k in ('VmPeak','VmSize','VmRSS','VmData','VmStk','VmExe'):
        if k in s: print(f'{k:8} {s[k]}')
if __name__=='__main__': main()
