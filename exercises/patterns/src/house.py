

class House:
    """All houses have rooms, a type of roof, and may have a porch."""
    def __init__(self):
        self.__rooms = list()
        self.__roof = None
        self.__porch = False

    def add_room(self, room):
        self.__rooms.append(room)

    def set_roof(self, roof):
        self.__roof = roof

    def set_porch(self, porch):
        self.__porch = porch

    def __str__(self):
        return 'rooms: ' + str(self.__rooms) + '\nroof: ' + self.__roof + '\nporch: ' + str(self.__porch)
