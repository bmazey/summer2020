from exercises.patterns.src.apartment_builder import ApartmentBuilder
from exercises.patterns.src.dream_mansion_builder import DreamMansionBuilder
from exercises.patterns.src.house_director import HouseDirector


def test_build_apartment():
    builder = ApartmentBuilder()
    director = HouseDirector(builder)
    house = director.get_house()
    print(str(house))

    builder_2 = DreamMansionBuilder()
    director = HouseDirector(builder_2)
    house = director. get_house()
    print(str(house))
 