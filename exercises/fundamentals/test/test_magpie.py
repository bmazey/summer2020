from exercises.fundamentals.src.zoo.magpie import Magpie


# steal emerald, ruby, sapphire
def test_basic_steal():
    magpie = Magpie('magpie', True, 0)
    magpie.steal('emerald')
    magpie.steal('ruby')
    magpie.steal('sapphire')

    assert 'emerald' in magpie.jewels
    assert 'ruby' in magpie.jewels
    assert 'sapphire' in magpie.jewels


def test_magpie_robbery():
    maggie = Magpie('maggie', True, 0)
    maggie.steal('emerald')
    maggie.steal('ruby')
    maggie.steal('sapphire')

    linda = Magpie('linda', True, 2)
    assert not linda.jewels

    linda.steal(maggie.robbed('emerald'))

    assert 'ruby' in maggie.jewels
    assert 'sapphire' in maggie.jewels
    assert 'emerald' not in maggie.jewels
    assert 'emerald' in linda.jewels
    # test linda stealing a diamond from maggie (diamond doesn't exist)

    linda.steal(maggie.robbed('diamond'))
    assert 'diamond' not in maggie.jewels
    assert 'diamond' not in linda.jewels