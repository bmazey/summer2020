from exercises.fundamentals.src.zoo.reptile import Reptile


def test_have_scales():
    cobra = Reptile('cobra', True, True, True)
    chameleon = Reptile('chameleon', True, True, True)
    chelidae = Reptile('chelidae', True, True, True)

    assert cobra.have_scales() == 'cobra have scales!'
    assert chameleon.have_scales() == 'chameleon have scales!'
    assert chelidae.have_scales() == 'chelidae have scales!'

def test_are_cold_blooded():
    gecko = Reptile('gecko', True, True, True)
    assert gecko.are_cold_blooded() == 'gecko is cold-blooded!'

def test_do_sunbathe():
    crocodile = Reptile('crocodile', True, True, True)
    assert crocodile.do_sunbathe() == 'crocodile sunbathe!'
