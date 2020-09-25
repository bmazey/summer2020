from exercises.patterns.src.house_builder import HouseBuilder


class ApartmentBuilder(HouseBuilder):
    def get_rooms(self):
        return ['bedroom', 'living room', 'dining room', 'bathroom']

    def get_roof(self):
        return 'slate'

    def get_porch(self):
        return False
