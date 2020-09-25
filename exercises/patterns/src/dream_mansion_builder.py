from exercises.patterns.src.house_builder import HouseBuilder


class DreamMansionBuilder(HouseBuilder):
    def get_rooms(self):
        return ['bedroom', 'master bedroom', 'bathroom', 'master bathroom', 'dining room', 'tea parlor', 'day room',
                'pool room', 'game room', 'servant\'s quarters']

    def get_roof(self):
        return 'japanese roof'

    def get_porch(self):
        return True
