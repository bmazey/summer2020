from exercises.fundamentals.src.zoo.animal import Animal


def test_create_animal():
    animal = Animal('platypus')
    assert animal.name == 'platypus'

    other_animal = Animal('kangaroo')
    assert other_animal.name == 'kangaroo'


def test_animal_breathe():
    tiger = Animal('tiger')
    breathe = tiger.breathe()
    assert breathe == 'tiger is breathing!'

    animal = Animal('kangaroo')
    breathe = animal.breathe()
    assert breathe == 'kangaroo is breathing!'


def test_animal_eat():
    lemur = Animal('lemur')
    eat = lemur.eat()
    assert eat == 'lemur is eating!'

    orca = Animal('orca')
    eat = orca.eat()
    assert eat == 'orca is eating!'
