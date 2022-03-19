import ast
import sys
import textdistance
import difflib
import os
import webbrowser
import time
import string


def antiplagiater(text_):    
    txt = ast.unparse(ast.parse(text_))   
    dump = ast.dump(ast.parse(txt), annotate_fields=False)[8:-6]

    for symbol in string.ascii_uppercase:
        dump = dump.replace(symbol, '#')

    for symbol in dump:
        if symbol not in ['(', ')', ',', "'", '#']:
            dump = dump.replace(symbol, '')

    while dump != dump.replace('##', '#'):
        dump = dump.replace('##', '#')
        
    dump = dump.replace("'#'", '')
    dump = dump.replace("''", '')
    dump = dump.replace('#)', ')')
    dump = dump.replace('#,', ',')
    return dump


with open(sys.argv[1]) as f:
    txt1 = f.read()

with open(sys.argv[2]) as f:
    txt2 = f.read()

dump1 = antiplagiater(txt1)
dump2 = antiplagiater(txt2)

dist = textdistance.damerau_levenshtein.normalized_distance(dump1, dump2)
print(dist)

if dist <= 0.1:
    html_diff = difflib.HtmlDiff()
    text = html_diff.make_file(txt1.split('\n'), txt2.split('\n'))
    with open('plagiat.html', 'w') as f:
        f.write(text)
    webbrowser.open('file://' + os.getcwd() + '/plagiat.html')
    time.sleep(1)
    os.remove('plagiat.html')    

 
