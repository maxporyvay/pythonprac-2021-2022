import gettext

translation = gettext.translation('tra', 'po', fallback=True)
_, ngettext = translation.gettext, translation.ngettext

def dialog():
    while s := input(_("Input a string: ")):
        n = len(s.split())
        print(ngettext('Entered {} word', 'Entered {} words', n).format(n))
        
if __name__ == '__main__':
    dialog()
