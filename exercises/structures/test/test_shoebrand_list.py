from exercises.structures.src.shoebrand_list import ShoeBrandList

brands = ['converse', 'vans', 'adidas']
mylist = ShoeBrandList(brands)


def test_shoebrand_list():
    # assert mylist.items[0] == brands[0]
    # assert mylist.items[1] == brands[1]
    # assert mylist.items[2] == brands[2]
    assert mylist.items == brands
