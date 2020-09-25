from exercises.fundamentals.src.zoo.bird import Bird


def test_bird_fly():
    pelican = Bird('pelican', True, 3)
    ostrich = Bird('ostrich', False, 1)
    peacock = Bird('peacock', True, 2)

    assert pelican.fly
    assert not ostrich.fly
    assert peacock.fly


def test_bird_make_nest():
    magpie = Bird('magpie', True, 4)
    assert magpie.make_nest() == 'magpie has made a nest!'


def test_bird_lay_eggs():
    penguin = Bird('penguin', False, 2)
    assert penguin.lay_eggs() == 'penguin has laid 2 eggs!'

    for i in range(100):
        penguin = Bird('penguin', False, 2)


def test_bird_eat_and_breathe():
    condor = Bird('condor', True, 1)
    assert condor.breathe() == 'condor is breathing!'
    assert condor.eat() == 'condor is eating!'
