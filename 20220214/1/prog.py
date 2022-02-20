import sys
import zlib
from glob import iglob
from os.path import basename, dirname

SHIFT = "  "

def viewCommitHistory(commitID):
    commit_name_dir, commit_name_file = commitID[:2], commitID[2:]
    commit_filepath = '.git/objects/' + commit_name_dir + '/' + commit_name_file
    obj = ''
    with open(commit_filepath, 'rb') as cf:
        obj = zlib.decompress(cf.read())
    objtext = obj.decode()
    print(objtext)
    _, objtext_ = objtext.split('tree ')
    isInitial = False
    if 'parent' in objtext:
        treename, parent = objtext_.split('\nparent ')
        parentID = parent.split()[0]
    else:
        isInitial = True
        treename, _ = objtext_.split('\nauthor')
    print('tree', treename)
    viewTree(treename, 1)
    print('-' * 80)
    if not isInitial:
        viewCommitHistory(parentID)

def viewTree(treeID, shiftcnt):
    treename_dir, treename_file = treeID[:2], treeID[2:]
    treename_filepath = '.git/objects/' + treename_dir + '/' + treename_file
    obj = ''
    with open(treename_filepath, 'rb') as tf:
        obj = zlib.decompress(tf.read())
    header, _, tail = obj.partition(b'\x00')
    kind, _ = header.split()
    if kind == b'tree':
        while tail:
            treeobj, _, tail = tail.partition(b'\x00')
            _, tname = treeobj.split()
            num, tail = tail[:20], tail[20:]
            num = num.hex()
            print(SHIFT * shiftcnt + f"{tname.decode()}")
            viewTree(num, shiftcnt + 1)

if len(sys.argv) == 1:
    for dr in iglob('.git/refs/heads/*'):
        print(basename(dr))
elif len(sys.argv) > 1:
    branch = sys.argv[1]
    branchpath = '.git/refs/heads/' + branch
    commit_name = ''
    with open(branchpath) as bp:
        commit_name = bp.readline().strip()
    viewCommitHistory(commit_name)
    
    

