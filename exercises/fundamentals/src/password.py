import random


def generate_password():
    # make a string called lowercase alphabet
    # contains letters a-z
    # same for uppercase A-Z
    # Same for digits 0-9
    # same for special characters !-*

    lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special_characters = '!@#$%^&*'

    password = ''

    for i in range(4):
        password += lowercase_alphabet[random.randint(0, len(lowercase_alphabet) - 1)]

    for i in range(4):
        password += str(random.randint(0, 9))

    for i in range(2):
        password += uppercase_alphabet[random.randint(0, len(uppercase_alphabet) - 1)]

    for i in range(2):
        password += special_characters[random.randint(0, len(special_characters) - 1)]

    return password
