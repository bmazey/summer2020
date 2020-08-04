from exercises.fundamentals.src.zoo.bird import Bird


class Magpie(Bird):
    """This is a class to define the properties and functions of magpies!"""

    def __init__(self, name, fly, eggs):
        super().__init__(name, fly, eggs)
        self.jewels = []

    def steal(self, jewel):
        if jewel is None:
            print(self.name + ' has failed to steal!')
            return

        print(self.name + ' has stolen a ' + jewel + '!')
        self.jewels.append(jewel)

    def robbed(self, jewel):
        if jewel in self.jewels:
            print(self.name + ' has been robbed of a ' + jewel + '!')
            self.jewels.remove(jewel)
            return jewel

        print(self.name + ' does not have a ' + jewel + '!')
        return None
