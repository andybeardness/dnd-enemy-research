class Perks:
    def __init__(
            self,
            p_str,
            p_dex,
            p_con,
            p_int,
            p_wis,
            p_cha,
    ):
        self.__p_str__ = self.__perk_filter__(p_str)
        self.__p_dex__ = self.__perk_filter__(p_dex)
        self.__p_con__ = self.__perk_filter__(p_con)
        self.__p_int__ = self.__perk_filter__(p_int)
        self.__p_wis__ = self.__perk_filter__(p_wis)
        self.__p_cha__ = self.__perk_filter__(p_cha)

    def __perk_filter__(self, perk):
        return perk if perk > 0 else 0

    def p_str(self):
        return self.__p_str__

    def p_dex(self):
        return self.__p_dex__

    def p_con(self):
        return self.__p_con__

    def p_int(self):
        return self.__p_int__

    def p_wis(self):
        return self.__p_wis__

    def p_cha(self):
        return self.__p_cha__


# TESTS

def tests_perks():
    perks = Perks(p_str=10, p_dex=12, p_con=14, p_int=16, p_wis=18, p_cha=20)
    assert perks.p_str() == 10
    assert perks.p_dex() == 12
    assert perks.p_con() == 14
    assert perks.p_int() == 16
    assert perks.p_wis() == 18
    assert perks.p_cha() == 20

    perks = Perks(p_str=-100, p_dex=-999, p_con=0, p_int=100, p_wis=999, p_cha=1)
    assert perks.p_str() == 0
    assert perks.p_dex() == 0
    assert perks.p_con() == 0
    assert perks.p_int() == 100
    assert perks.p_wis() == 999
    assert perks.p_cha() == 1


tests_perks()
