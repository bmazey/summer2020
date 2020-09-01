from exercises.structures.src.x_y_z_map import MapXYZ

xyz = MapXYZ()
xyz.populate_map('eye patch', 'treasure chest', 'macaw')


def test_key_x():
    assert xyz.map['x'] == 'eye patch'.casefold()


def test_key_y():
    assert xyz.map['y'] == 'treasure chest'.casefold()


def test_key_z():
    assert xyz.map['z'] == 'macaw'.casefold()
