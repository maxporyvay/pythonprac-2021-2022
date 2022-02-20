import sys
import zlib
from glob import iglob
from os.path import basename, dirname

SHIFT = "  "

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
    objtext = obj.decode()
    print(objtext)
    _, objtext_ = objtext.split('tree ')
    if 'parent' in objtext:
        treename, _ = objtext_.split('\nparent')
    else:
        treename, _ = objtext_.split('\nauthor')
    print('tree', treename)
    treename_dir, treename_file = treename[:2], treename[2:]
    treename_filepath = '.git/objects/' + treename_dir + '/' + treename_file
    obj = ''
    with open(treename_filepath, 'rb') as tf:
        obj = zlib.decompress(tf.read())
    _, _, tail = obj.partition(b'\x00')
    while tail:
        treeobj, _, tail = tail.partition(b'\x00')
        tmode, tname = treeobj.split()
        num, tail = tail[:20], tail[20:]
        print(f"{SHIFT}{tname.decode()} {tmode.decode()} {num.hex()}")

