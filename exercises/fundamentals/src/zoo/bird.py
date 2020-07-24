from exercises.fundamentals.src.zoo.animal import Animal


class Bird(Animal):
    """This is a class to define the properties and functions of all birds!"""

    # all birds fly and lay eggs
    def __init__(self, name, fly, eggs):
        super().__init__(name)
        self.fly = fly
        self.eggs = eggs

    # all birds make nests
    def make_nest(self):
        return self.name + ' has made a nest!'

    # all birds lay eggs
    def lay_eggs(self):
        return self.name + ' has laid ' + str(self.eggs) + ' eggs!'
