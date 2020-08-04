from exercises.fundamentals.src.zoo.amphibian import Amphibian
from exercises.fundamentals.src.zoo.frog import Frog


def test_amphibian_swim():
    tadpole = Amphibian('tadpole')
    tadpole.swim()


def test_amphibian_transform():
    kermit = Amphibian('kermit')
    kermit.swim()

    kermit.transform()
    kermit.hop()


def test_amphibian_string():
    jelly = Frog('jelly', 4)
    print(str(jelly))
