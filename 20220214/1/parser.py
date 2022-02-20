import sys
import zlib
from glob import iglob
from os.path import basename, dirname

if len(sys.argv) == 1:
    for dr in iglob('.git/refs/heads/*'):
        print(basename(dr))
elif len(sys.argv) > 1:
    branch = sys.argv[1]
    branchpath = '.git/refs/heads/' + branch
    commit_name = ''
    with open(branchpath) as bp:
        commit_name = bp.readline().strip()
    commit_name_dir, commit_name_file = commit_name[:2], commit_name[2:]
    commit_filepath = '.git/objects/' + commit_name_dir + '/' + commit_name_file
    obj = ''
    with open(commit_filepath, 'rb') as cf:
        obj = zlib.decompress(cf.read())
    print(obj.decode())
