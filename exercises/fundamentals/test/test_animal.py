from exercises.fundamentals.src.zoo.animal import Animal
from exercises.fundamentals.src.zoo.bird import Bird
from exercises.fundamentals.src.zoo.mammal import Mammal
from exercises.fundamentals.src.zoo.reptile import Reptile


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


def test_all_animals():
    # make a bird - 'turkey'; make a mammal - 'otter'; make a reptile - 'gila monster',

    orangutan = Animal('orangutan')
    turkey = Bird('turkey', True, 2)
    otter = Mammal('otter', True, True)
    gila_monster = Reptile('gila monster', True, True, True)

    animals = [orangutan, turkey, otter, gila_monster]

    for animal in animals:
        print(animal.eat())
        print(animal.breathe())
