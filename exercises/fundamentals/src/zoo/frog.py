from exercises.fundamentals.src.zoo.animal import Animal


class Frog(Animal):
    """This is a class to define the properties and functions of all frogs!"""

    # all frogs have 4 legs
    def __init__(self, name, legs):
        super().__init__(name)
        self.legs = legs

    def __str__(self):
        return '\nname: {}\nnumber of legs: {}'.format(self.name, str(self.legs))

    def hop(self):
        print(self.name + ' is hopping with ' + str(self.legs) + ' legs!')

