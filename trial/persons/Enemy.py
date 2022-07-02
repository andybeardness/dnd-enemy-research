from trial.models.Weapon import Weapon
from trial.models.Health import Health
from trial.models.Armor import Armor


class Enemy:
    def __init__(self,
                 weapon_dice, weapon_modifier,
                 max_health, current_health,
                 armor):

        self.__weapon__ = Weapon(
            dice=weapon_dice,
            modifier=weapon_modifier,
        )

        self.__health__ = Health(
            max_health=max_health,
            current_health=current_health,
        )

        self.__armor__ = Armor(
            armor=armor
        )

    def is_alive(self):
        return self.__health__.is_alive()

    def damage(self, damage):
        self.__health__.damage(damage=damage)

    def heal(self, heal):
        self.__health__.heal(heal=heal)

    def current_health(self):
        return self.__health__.current_health()

    def max_health(self):
        return self.__health__.max_health()

    def armor(self):
        return self.__armor__.armor()

    def is_hit(self, hits):
        return self.__armor__.is_hit(hits=hits)

    def attack(self):
        return self.__weapon__.attack()
