from exercises.fundamentals.src.zoo.mammal import Mammal


def test_is_warm_blooded():
    microbat = Mammal('microbat', True, True)
    mandrill = Mammal('mandrill', True, True)
    culpeo = Mammal('culpeo', True, True)

    assert microbat.is_warm_blooded() == 'microbat is warm-blooded!'
    assert mandrill.is_warm_blooded() == 'mandrill is warm-blooded!'
    assert culpeo.is_warm_blooded() == 'culpeo is warm-blooded!'


def test_have_sweat_glands():
    dolphin = Mammal('dolphin', True, True)
    assert dolphin.have_sweat_glands() == 'dolphin has sweat glands!'
