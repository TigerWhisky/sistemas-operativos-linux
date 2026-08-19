import os,sys
sys.path.insert(0,'src')
from filesystem.file_permissions import describe_mode
from memory.proc_memory import read_status
from threads.mutex_counter import run_once
def test_mode(): assert describe_mode(0o100644)=='-rw-r--r--'
def test_memory():
    if os.path.exists('/proc/self/status'): assert 'VmRSS' in read_status()
def test_mutex(): assert run_once()==400000
