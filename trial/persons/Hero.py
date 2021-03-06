from trial.models.Perks import Perks
from trial.models.Modifiers import Modifiers
from trial.models.Weapon import Weapon
from trial.models.Health import Health
from trial.models.Armor import Armor


class Hero:
    def __init__(self,
                 h_str, h_dex, h_con, h_int, h_wis, h_cha,
                 weapon_dice, weapon_modifier,
                 max_health, current_health,
                 armor):

        self.__perks__ = Perks(
            p_str=h_str,
            p_dex=h_dex,
            p_con=h_con,
            p_int=h_int,
            p_wis=h_wis,
            p_cha=h_cha,
        )

        self.__modifiers__ = Modifiers(
            m_str=h_str,
            m_dex=h_dex,
            m_con=h_con,
            m_int=h_int,
            m_wis=h_wis,
            m_cha=h_cha,
        )

        self.__weapon__ = Weapon(
            dice=weapon_dice,
            modifier=weapon_modifier,
        )

        self.__health__ = Health(
            max_health=max_health,
            current_health=current_health,
        )

        self.__armor__ = Armor(
            armor=armor,
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
