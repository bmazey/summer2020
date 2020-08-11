from exercises.expressions.src.hieroglyph import Hieroglyph


def test_sacred_cat():
    # all cats are sacred!
    assert not Hieroglyph.worship_sacred_cats('dog dog dog')
    assert Hieroglyph.worship_sacred_cats('cat')
    assert Hieroglyph.worship_sacred_cats('dog cat dog dog')
    assert Hieroglyph.worship_sacred_cats('scarab cat scarab cat')
    assert Hieroglyph.worship_sacred_cats('cat cat ')


def test_alphanumeric_glyph():
    assert Hieroglyph.alphanumeric_glyph('wxyd67891')
    assert not Hieroglyph.alphanumeric_glyph('ad143')
    assert not Hieroglyph.alphanumeric_glyph('34561')
    assert not Hieroglyph.alphanumeric_glyph('sand pyramid')
    assert Hieroglyph.alphanumeric_glyph('gold2134598')
    assert Hieroglyph.alphanumeric_glyph('sand104923')
    assert not Hieroglyph.alphanumeric_glyph('143sand')


def test_steal_crystal_skull():
    assert Hieroglyph.steal_crystal_skull('crystal skull') == 'crystal idol'
    assert Hieroglyph.steal_crystal_skull('skull crystal skull') == 'idol crystal idol'
    assert Hieroglyph.steal_crystal_skull('crystal boulder') == 'crystal boulder'
    assert Hieroglyph.steal_crystal_skull('skull skull boulder skull') == 'idol idol boulder idol'


def test_symbolic_glyph():
    assert Hieroglyph.symbolic_glyph('%@')
    assert not Hieroglyph.symbolic_glyph('@')
    assert not Hieroglyph.symbolic_glyph('@%')
    assert Hieroglyph.symbolic_glyph('%%%@@@')
    assert Hieroglyph.symbolic_glyph('%%%#@@@')
    assert Hieroglyph.symbolic_glyph('%%%###@@@')
    assert not Hieroglyph.symbolic_glyph('#')
    assert not Hieroglyph.symbolic_glyph('#%')


def test_nile_crocodile():
    assert Hieroglyph.nile_crocodile('nile crocodile')
    assert not Hieroglyph.nile_crocodile('crocodile')
    assert not Hieroglyph.nile_crocodile('nile')
    assert Hieroglyph.nile_crocodile('beware the nile crocodile')
