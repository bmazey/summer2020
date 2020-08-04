from exercises.fundamentals.src.zoo.animal import Animal
from exercises.fundamentals.src.zoo.frog import Frog


class Amphibian(Animal):
    """This is a class to define the properties and functions of all amphibians!"""

    # all birds fly and lay eggs
    def __init__(self, name):
        super().__init__(name)
        self.cold_blooded = True
        self.legs = 0

    def swim(self):
        print(self.name + ' is swimming with ' + str(self.legs) + ' legs!')

    def transform(self):
        # return Frog(self.name, 4)
        self.__class__ = Frog
        self.__dict__['legs'] = 4
