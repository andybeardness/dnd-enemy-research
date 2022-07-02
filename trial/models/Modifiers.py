def calculate_modifier(modifier):
    if modifier <= 0:
        return 0

    based = modifier - 10

    if based <= 0:
        return 0

    divided = based / 2

    modifier = int(divided)

    return modifier


class Modifiers:
    def __init__(self, m_str, m_dex, m_con, m_int, m_wis, m_cha):
        self.__m_str__ = calculate_modifier(m_str)
        self.__m_dex__ = calculate_modifier(m_dex)
        self.__m_con__ = calculate_modifier(m_con)
        self.__m_int__ = calculate_modifier(m_int)
        self.__m_wis__ = calculate_modifier(m_wis)
        self.__m_cha__ = calculate_modifier(m_cha)

    def m_str(self):
        return self.__m_str__

    def m_dex(self):
        return self.__m_dex__

    def m_con(self):
        return self.__m_con__

    def m_int(self):
        return self.__m_int__

    def m_wis(self):
        return self.__m_wis__

    def m_cha(self):
        return self.__m_cha__


# TESTS

def modifiers_test():
    modifiers = Modifiers(m_str=10, m_dex=12, m_con=14, m_int=8, m_wis=6, m_cha=2)

    assert modifiers.m_str() == 0
    assert modifiers.m_dex() == 1
    assert modifiers.m_con() == 2
    assert modifiers.m_int() == 0
    assert modifiers.m_wis() == 0
    assert modifiers.m_cha() == 0

    modifiers = Modifiers(m_str=-100, m_dex=11, m_con=15, m_int=-999, m_wis=0, m_cha=12)

    assert modifiers.m_str() == 0
    assert modifiers.m_dex() == 0
    assert modifiers.m_con() == 2
    assert modifiers.m_int() == 0
    assert modifiers.m_wis() == 0
    assert modifiers.m_cha() == 1


if __name__ == '__main__':
    modifiers_test()
