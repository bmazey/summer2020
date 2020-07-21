

class Animal:
    """This is a class to define the properties and functions of all animals."""

    # all animals have a name
    def __init__(self, name):
        self.name = name

    # all animals breathe and eat
    def breathe(self):
        return self.name + ' is breathing!'

    def eat(self):
        return self.name + ' is eating!'
