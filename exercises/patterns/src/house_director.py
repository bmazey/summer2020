from exercises.patterns.src.house import House


class HouseDirector:
    def __init__(self, builder):
        self.__builder = builder

    def get_house(self):
        house = House()

        rooms = self.__builder.get_rooms()
        for room in rooms:
            house.add_room(room)

        roof = self.__builder.get_roof()
        house.set_roof(roof)

        porch = self.__builder.get_porch()
        house.set_porch(porch)

        return house
