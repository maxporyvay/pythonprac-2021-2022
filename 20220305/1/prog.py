import readline
import shlex
import cmd
from random import randint


class Repl(cmd.Cmd):
    
    prompt = '>'

    def __init__(self):
        super(Repl, self).__init__()
        self.field = [[0 for _ in range(10)] for _ in range(10)]
        self.player_coords = (randint(0, 9), randint(0, 9))
        print('player at', *(self.player_coords))
        self.monsters = {}

    def do_attack(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            return

    def do_move(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            return

    def do_show(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            return

    def do_add(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            return

    def complete_attack(self, text, line, begidx, endidx):
        pass

    def complete_move(self, text, line, begidx, endidx):
        pass
    
    def do_exit(self, arg):
        return True


Repl().cmdloop()
