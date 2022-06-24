import random

class Weapon:
    def __init__(self, dice, modifier):
        self.__dice__ = dice
        self.__modifier__ = modifier

    def __attack__(self):
        return random.randint(1, self.__dice__) + self.__modifier__


def test_loop_min_max(weapon, loops):
    _min = None
    _max = None

    for _ in range(0, loops):
        attack = weapon.__attack__()

        if (_min is None or attack < _min):
            _min = attack

        if ( _max is None or attack > _max):
            _max = attack

    return _min, _max


def test_weapon():
    loops = 1_000_000

    weapon = Weapon(8, 0)
    _min, _max = test_loop_min_max(weapon=weapon, loops=loops)

    assert _min == 1
    assert _max == 8

test_weapon()
