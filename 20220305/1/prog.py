import readline
import shlex
import cmd


class Repl(cmd.Cmd):
    
    prompt = '>'

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
