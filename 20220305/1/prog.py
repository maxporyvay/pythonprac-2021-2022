import readline
import shlex
import cmd


class Repl(cmd.Cmd):
    
    prompt = '>'

    def __init__(self):
        super(Repl, self).__init__()
        self.field = [[0 for _ in range(10)] for _ in range(10)]
        self.player_coords = (0, 0)
        print('player at', *(self.player_coords))
        self.monsters = {}
        print('Please, don\'t use "_" in monsters\' names - use spaces instead')

    def do_attack(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            return
        else:
            if len(args) == 1:
                args[0] = ' '.join(args[0].split('_'))
                if args[0] in self.monsters and self.player_coords in self.monsters[args[0]]:
                    hp = self.monsters[args[0]][self.player_coords]
                    hp -= 10
                    if hp > 0:
                        print(f'{args[0]} lost 10 hp, now has {hp} hp')
                        self.monsters[args[0]][self.player_coords] -= 10
                    else:
                        print(f'{args[0]} dies')
                        self.monsters[args[0]].pop(self.player_coords)
                        if not self.monsters[args[0]]:
                            self.monsters.pop(args[0])
                else:
                    print(f'no {args[0]} here')
            else:
                print('Failed')

    def after_move(self):
        print('player at', *(self.player_coords))
        flag = False
        string = ''
        for name, dct in self.monsters.items():
            for coords, hp in dct.items():
                if self.player_coords == coords:
                    flag = True
                    string += f' {name} hp {hp},'
        if flag:
            print('encountered:', string[:-1], sep='')
        

    def do_move(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            return
        else:
            if len(args) == 1:
                match(args[0]):
                    case 'up':
                        if self.player_coords[1] != 0:
                            self.player_coords = (self.player_coords[0], self.player_coords[1] - 1)
                            self.after_move()
                        else:
                            print('cannot move')
                    case 'down':
                        if self.player_coords[1] != 9:
                            self.player_coords = (self.player_coords[0], self.player_coords[1] + 1)
                            self.after_move()
                        else:
                            print('cannot move')
                    case 'left':
                        if self.player_coords[0] != 0:
                            self.player_coords = (self.player_coords[0] - 1, self.player_coords[1])
                            self.after_move()
                        else:
                            print('cannot move')
                    case 'right':
                        if self.player_coords[0] != 9:
                            self.player_coords = (self.player_coords[0] + 1, self.player_coords[1])
                            self.after_move()
                        else:
                            print('cannot move')
                    case _:
                        print('Failed')
            else:
                print('Failed')
            

    def do_show(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            return
        else:
            if len(args) == 1 and args[0] == 'monsters':
                for name, dct in self.monsters.items():
                    for coords, hp in dct.items():
                        print(f'{name} at ({coords[0]} {coords[1]}) hp {hp}')
            else:
                print('Failed')

    def do_add(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            return
        else:
            if len(args) == 8:
                m, n, name, h, hp, c, cx, cy = args
                if m == 'monster' and n == 'name' and h == 'hp' and c == 'coords' and hp.isdigit() and cx.isdigit() and cy.isdigit():
                    hp = int(hp)
                    cx = int(cx)
                    cy = int(cy)
                    if hp > 0 and cx in range(10) and cy in range(10):
                        if name in self.monsters:
                            self.monsters[name][(cx, cy)] = hp
                        else:
                            self.monsters[name] = {(cx, cy): hp}
                    else:
                        print('Failed')
                else:
                    print('Failed')
            else:
                print('Failed')

    def complete_attack(self, text, line, begidx, endidx):
        if line.count(' ') == 1:
            ls = []
            for name, dct in self.monsters.items():
                for coords, hp in dct.items():
                    if self.player_coords == coords:
                        ls.append(name.replace(' ', '_'))
            return [s for s in ls if s.startswith(text)]

    def complete_move(self, text, line, begidx, endidx):
        return [s for s in ['up', 'down', 'left', 'right'] if s.startswith(text)]
    
    def do_exit(self, arg):
        return True


Repl().cmdloop()
