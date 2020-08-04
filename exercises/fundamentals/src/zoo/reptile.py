from exercises.fundamentals.src.zoo.animal import Animal


class Reptile(Animal):
    """This is a class to define the properties and functions of all reptiles!"""

    # all reptiles fly and lay eggs
    def __init__(self, name, scales, cold_blooded, sunbathe):
        super().__init__(name)
        self.scales = scales
        self.sunbathe = sunbathe
        self.cold_blooded = cold_blooded

    # all reptiles have scales
    def have_scales(self):
        return self.name + ' have scales!'

    # all reptiles are cold-blooded
    def are_cold_blooded(self):
        return self.name + ' is cold-blooded!'

    # all reptile sunbathe
    def do_sunbathe(self):
        return self.name + ' sunbathe!'
