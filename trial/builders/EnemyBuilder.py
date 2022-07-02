import random

from trial.models.Perks import default_perks
from trial.persons.Enemy import Enemy

def build_random_enemy():
    weapon_dice = random.randint(0, 3)
    weapon_dice = weapon_dice * 2
    weapon_dice = weapon_dice + 4

    is_milli = random.choice([True, False])
    weapon_modifier = random.choice(default_perks().copy())

    health = random.randint(6, 16)
    armor = random.randint(8, 16)

    enemy = Enemy(weapon_dice=weapon_dice, weapon_modifier=weapon_modifier,
                  max_health=health, current_health=health,
                  armor=armor)

    return enemy

