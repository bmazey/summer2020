# at least 12 characters long
# contain at least 4 lowercase letters
# contain at least 4 digits
# contain at least 2 uppercase letters
# contain at least 2 special characters
from exercises.fundamentals.src.password import generate_password


def test_password_length():
    # password = generate_password()
    assert len(generate_password()) == 12


def test_password_lowercase():
    password = generate_password()
    assert password[0].isalpha()
    assert password[1].isalpha()
    assert password[2].isalpha()
    assert password[3].isalpha()


def test_password_digits():
    password = generate_password()
    assert password[4].isdigit()
    assert password[5].isdigit()
    assert password[6].isdigit()
    assert password[7].isdigit()


def test_password_uppercase():
    password = generate_password()
    assert password[8].isalpha()
    assert password[9].isalpha()


def test_password_special():
    password = generate_password()
    assert contains_any(password[10], '!@#$%^&*')


def contains_any(str, set):
    """ Check whether sequence str contains ANY of the items in set. """
    return 1 in [c in str for c in set]
