import random

from trial.models.Perks import default_perks
from trial.persons.Hero import Hero
from trial.models.Modifiers import calculate_modifier


def build_random_default_hero():
    shuffled_perks = default_perks().copy()
    random.shuffle(shuffled_perks)

    b_str = shuffled_perks[0]
    b_dex = shuffled_perks[1]
    b_con = shuffled_perks[2]
    b_int = shuffled_perks[3]
    b_wis = shuffled_perks[4]
    b_cha = shuffled_perks[5]

    weapon_dice = random.randint(0, 3)
    weapon_dice = weapon_dice * 2
    weapon_dice = weapon_dice + 4

    is_milli = random.choice([True, False])
    weapon_modifier = b_str if (is_milli) else b_dex
    weapon_modifier = calculate_modifier(weapon_modifier)

    health = random.randint(6, 16)
    armor = random.randint(8, 16)

    hero = Hero(
        h_str=b_str,
        h_dex=b_dex,
        h_con=b_con,
        h_int=b_int,
        h_wis=b_wis,
        h_cha=b_cha,
        weapon_dice=weapon_dice,
        weapon_modifier=weapon_modifier,
        max_health=health,
        current_health=health,
        armor=armor,
    )

    return hero