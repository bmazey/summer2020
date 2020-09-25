from exercises.patterns.src.sword import Sword, UnbreakableSword, MasterSword


def test_swing_sword():
    rapier = Sword()
    assert not rapier.broken
    for i in range(101):
        rapier.swing()
    assert rapier.num_uses <= 0
    assert rapier.broken
    print(rapier.__repr__())
    rapier = Sword()
    print(rapier.__repr__())
    print(rapier.num_uses)


def test_swing_unbreakable():
    estoc = UnbreakableSword()
    assert not estoc.disappear
    for i in range(101):
        estoc.swing_unbreakable()
    assert estoc.num_uses <= 0
    assert estoc.disappear


def test_master_sword():
    player_1 = MasterSword.get_instance()
    player_1.swing()
    print(player_1.num_uses)
    print(player_1.__repr__())

    player_2 = MasterSword.get_instance()
    player_2.swing()
    print(player_2.num_uses)
    print(player_2.__repr__())

    player_3 = MasterSword()
    player_3.swing()
