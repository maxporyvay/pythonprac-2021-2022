from pyfiglet import Figlet
import gettext
import os

def solve(a, b):
    if a == 0:
        return None
    else:
        return -b / a

def main():
    translation = gettext.translation('lineq', os.path.dirname(__file__) + '/po', fallback=True)
    _ = translation.gettext
    a = float(input())
    b = float(input())
    res = solve(a, b)
    if res is None:
        if b != 0:
            print(Figlet(font='graceful').renderText(_('NO ROOTS')))
        else:
            print(Figlet(font='graceful').renderText(_('(-INF, +INF)')))
    else:
        text = _('Root: {}').format(res)
        print(Figlet(font='graceful').renderText(text))
        

if __name__ == '__main__':
    main() 
