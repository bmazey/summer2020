from exercises.fundamentals.src.fizzbuzz import fizzbuzz


def test_fizzbuzz():
    output = fizzbuzz(9)
    assert output == 'fizz'

    output = fizzbuzz(10)
    assert output == 'buzz'

    output = fizzbuzz(15)
    assert output == 'fizzbuzz'

    output = fizzbuzz(13)
    assert output == ''