import shlex
import cmd
import sys
from MUD.game import Game

game = Game()


class Repl(cmd.Cmd):

    prompt = '>'

    def __init__(self):
        super(Repl, self).__init__()
        self.game = game
        print('player at', *(self.game.player_coords))
        print('Please, don\'t use "_" in monsters\' names - use spaces instead')

    def do_attack(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            return
        else:
            if len(args) == 1:
                args[0] = ' '.join(args[0].split('_'))
                if any([args[0] == monster.name for monster in self.game.monsters]) and any([self.game.player_coords == monster.monster_coords
                                                                                             for monster in self.game.monsters if args[0] == monster.name]):
                    monster = [monster for monster in self.game.monsters if args[0] == monster.name and self.game.player_coords == monster.monster_coords][0]
                    monster.hp -= 10
                    if monster.hp > 0:
                        print(f'{args[0]} lost 10 hp, now has {monster.hp} hp')
                    else:
                        print(f'{args[0]} dies')
                        self.game.monsters.remove(monster)
                else:
                    print(f'no {args[0]} here')
            else:
                print('Failed')

    def after_move(self):
        print('player at', *(self.game.player_coords))
        flag = False
        string = ''
        for monster in self.game.monsters:
            if self.game.player_coords == monster.monster_coords:
                flag = True
                string += f' {monster.name} hp {monster.hp},'
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
                        if self.game.player_coords[1] != 0:
                            self.game.player_coords = (self.game.player_coords[0], self.game.player_coords[1] - 1)
                            self.after_move()
                        else:
                            print('cannot move')
                    case 'down':
                        if self.game.player_coords[1] != 9:
                            self.game.player_coords = (self.game.player_coords[0], self.game.player_coords[1] + 1)
                            self.after_move()
                        else:
                            print('cannot move')
                    case 'left':
                        if self.game.player_coords[0] != 0:
                            self.game.player_coords = (self.game.player_coords[0] - 1, self.game.player_coords[1])
                            self.after_move()
                        else:
                            print('cannot move')
                    case 'right':
                        if self.game.player_coords[0] != 9:
                            self.game.player_coords = (self.game.player_coords[0] + 1, self.game.player_coords[1])
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
                for monster in self.game.monsters:
                    print(f'{monster.name} at ({monster.monster_coords[0]} {monster.monster_coords[1]}) hp {monster.hp}')
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
                        self.game.add_monster((cx, cy), hp, name)
                    else:
                        print('Failed')
                else:
                    print('Failed')
            else:
                print('Failed')

    def complete_attack(self, text, line, begidx, endidx):
        if line.count(' ') == 1:
            ls = []
            for monster in self.game.monsters:
                if self.game.player_coords == monster.monster_coords:
                    ls.append(monster.name.replace(' ', '_'))
            return [s for s in ls if s.startswith(text)]

    def complete_move(self, text, line, begidx, endidx):
        return [s for s in ['up', 'down', 'left', 'right'] if s.startswith(text)]

    def do_exit(self, arg):
        return True


def main():
    Repl().cmdloop(game)


if __name__ == '__main__':
    sys.exit(main())
