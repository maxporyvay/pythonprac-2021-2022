import ipsedixit
import sys

assert len(sys.argv) == 3

count = int(sys.argv[1])
cipher = sys.argv[2]
if cipher != 'tacitus' and cipher != 'caesar':
    with open(cipher, encoding='utf-8') as f:
        cipher = f.read()

generator = ipsedixit.Generator(cipher)
paragraphs = generator.paragraphs(count)

print(*paragraphs, sep='\n\n')
