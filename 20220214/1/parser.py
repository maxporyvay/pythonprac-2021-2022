import zlib
from glob import iglob
from os.path import basename, dirname

for dr in iglob('.git/refs/heads/*'):
    print(basename(dr))
