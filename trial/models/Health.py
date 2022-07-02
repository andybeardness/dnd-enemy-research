class Health:
    def __init__(self, max_health, current_health=None):
        self.__max_health__ = max_health

        if current_health is None and max_health >= 0:
            self.__current_health__ = max_health
            return

        if current_health is None and max_health < 0:
            self.__max_health__ = 1
            self.__current_health__ = self.__max_health__
            return

        if max_health < 0 and current_health < 0:
            self.__max_health__ = 1
            self.__current_health__ = 1
            return

        if current_health > max_health:
            self.__current_health__ = max_health
        elif current_health < 0:
            self.__current_health__ = 0
        else:
            self.__current_health__ = current_health

    def damage(self, damage):
        if damage <= 0:
            return

        if self.__current_health__ <= 0:
            self.__current_health__ = 0
            return

        self.__current_health__ = self.__current_health__ - damage

        if self.__current_health__ < 0:
            self.__current_health__ = 0
            return

    def heal(self, heal):
        if heal <= 0:
            return

        if self.__current_health__ <= 0:
            return

        self.__current_health__ += heal

    def alive(self, current_health):
        if self.__current_health__ != 0:
            return

        if current_health <= 0:
            return

        if current_health > self.__max_health__:
            self.__current_health__ = self.__max_health__
        else:
            self.__current_health__ = current_health

    def is_alive(self):
        return self.__current_health__ > 0

    def max_health(self):
        return self.__max_health__

    def current_health(self):
        return self.__current_health__


# TESTS
def health_test_init():
    health = Health(max_health=100)
    assert health.current_health() == health.max_health() == 100
    assert health.is_alive()

    health = Health(max_health=20, current_health=10)
    assert health.current_health() == 10
    assert health.max_health() == 20
    assert health.is_alive()

    health = Health(max_health=20, current_health=30)
    assert health.current_health() == health.max_health() == 20
    assert health.is_alive()

    health = Health(max_health=-100)
    assert health.current_health() == health.max_health() == 1
    assert health.is_alive()

    health = Health(max_health=100, current_health=-100)
    assert health.current_health() == 0
    assert health.max_health() == 100
    assert not health.is_alive()

    health = Health(max_health=100, current_health=0)
    assert not health.is_alive()


def health_test_damage():
    health = Health(max_health=100, current_health=50)

    health.damage(20)
    assert health.current_health() == 30
    assert health.is_alive()

    health.damage(20)
    assert health.current_health() == 10
    assert health.is_alive()

    health.damage(-100)
    assert health.current_health() == 10
    assert health.is_alive()

    health.damage(20)
    assert health.current_health() == 0
    assert not health.is_alive()


def health_test_heal():
    health = Health(max_health=100, current_health=10)
    health.heal(20)
    assert health.current_health() == 30
    assert health.is_alive()

    health.heal(20)
    assert health.current_health() == 50
    assert health.is_alive()

    health.heal(-100)
    assert health.current_health() == 50
    assert health.is_alive()

    health = Health(max_health=100, current_health=0)
    health.heal(10)
    assert health.current_health() == 0
    assert not health.is_alive()


def health_test_alive():
    health = Health(max_health=100, current_health=10)
    health.alive(current_health=20)
    assert health.is_alive()
    assert health.current_health() == 10

    health = Health(max_health=100, current_health=0)
    health.alive(current_health=20)
    assert health.is_alive()
    assert health.current_health() == 20

    health = Health(max_health=100, current_health=0)
    health.alive(current_health=200)
    assert health.is_alive()
    assert health.current_health() == health.max_health()


def health_test():
    health_test_init()
    health_test_damage()
    health_test_heal()


if __name__ == '__main__':
    health_test()
