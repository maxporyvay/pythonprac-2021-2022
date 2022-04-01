"""Модуль game предназначен для описания логики MUD."""


class Game():
    """Класс Game предназначен для реализации основных игровых механик MUD."""

    def __init__(self):
        """Функция __init__ предназначена для инициализации параметров MUD."""
        # self.field = [[0 for _ in range(10)] for _ in range(10)]
        self.player_coords = (0, 0)
        self.monsters = []

    def add_monster(self, coords, hp, name):
        """Функция add_monster предназначена для добавления нового монстра в MUD."""
        if not any([name == monster.name for monster in self.monsters]):
            self.monsters.append(Monster(coords, hp, name))
        elif not any([coords == monster.monster_coords for monster in self.monsters if name == monster.name]):
            self.monsters.append(Monster(coords, hp, name))
        else:
            monster = [monster for monster in self.monsters if name == monster.name and coords == monster.monster_coords][0]
            monster.hp = hp


class Monster():
    """Класс Monster предназначен для описания монстров в MUD."""

    def __init__(self, coords, hp, name):
        """Функция __init__ предназначена для инициализации параметров монстра в MUD."""
        self.monster_coords = coords
        self.hp = hp
        self.name = name
