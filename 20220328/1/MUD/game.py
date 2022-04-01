class Game():

    def __init__(self):
        # self.field = [[0 for _ in range(10)] for _ in range(10)]
        self.player_coords = (0, 0)
        self.monsters = []

    def add_monster(self, coords, hp, name):
        if not any([name == monster.name for monster in self.monsters]):
            self.monsters.append(Monster(coords, hp, name))
        elif not any([coords == monster.monster_coords for monster in self.monsters if name == monster.name]):
            self.monsters.append(Monster(coords, hp, name))
        else:
            monster = [monster for monster in self.monsters if name == monster.name and coords == monster.monster_coords][0]
            monster.hp = hp


class Monster():

    def __init__(self, coords, hp, name):
        self.monster_coords = coords
        self.hp = hp
        self.name = name
