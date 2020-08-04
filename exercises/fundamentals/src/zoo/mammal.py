from exercises.fundamentals.src.zoo.animal import Animal


class Mammal(Animal):
    """This is a class to define the properties and functions of all mammals!"""

    # all mammals fly and lay eggs
    def __init__(self, name, warm_blooded, sweat_glands):
        super().__init__(name)
        self.warm_blooded = warm_blooded
        self.sweat_glands = sweat_glands

    # all mammals are warm-blooded
    def is_warm_blooded(self):
        return self.name + ' is warm-blooded!'

    # all mammals have sweat glands
    def have_sweat_glands(self):
        return self.name + ' has sweat glands!'
