class Armor:
    def __init__(self, armor):
        if armor <= 0:
            self.__armor__ = 1
        else:
            self.__armor__ = armor

    def armor(self):
        return self.__armor__

    def is_hit(self, hits):
        return hits >= self.__armor__


def test_armor():
    armor = Armor(10)
    assert armor.armor() == 10
    assert armor.is_hit(hits=10)
    assert armor.is_hit(hits=14)
    assert armor.is_hit(hits=20)
    assert not armor.is_hit(hits=2)
    assert not armor.is_hit(hits=1)
    assert not armor.is_hit(hits=-1)

    armor = Armor(-5)
    assert armor.armor() == 1
    assert armor.is_hit(hits=10)
    assert armor.is_hit(hits=14)
    assert armor.is_hit(hits=20)
    assert armor.is_hit(hits=2)
    assert armor.is_hit(hits=1)
    assert not armor.is_hit(hits=-1)

test_armor()