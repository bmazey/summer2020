import random
# define a method called XOR
    # XOR should take two binaries and return a new binary
# generate key
    # generate a random binary value that matches the length of the plaintext
# have an encrypt method
    # method should take a plaintext and key to return a ciphertext
# have a decrypt method
    # method should take ciphertext and key to return the original plaintext
# encode/decode
    # converts to and from strings and binary numbers


# TODO: encode whitespace and special characters
def encode(text):
    return ''.join(format(ord(i), 'b') for i in text)


def decode(binary):
    str_data = ''

    for i in range(0, len(binary), 7):
        temp_data = int(binary[i:i + 7])
        decimal_data = binary_to_decimal(temp_data)
        str_data = str_data + chr(decimal_data)

    return str_data


def binary_to_decimal(binary):
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def generate_key(size):
    key = ''

    for i in range(size):
        key += str(random.randint(0, 1))

    return key


def encrypt(encoded, key):
    ciphertext = int(encoded, 2) ^ int(key, 2)
    return '{0:b}'.format(ciphertext)


def decrypt(ciphertext, key):
    plaintext = int(ciphertext, 2) ^ int(key, 2)
    return '{0:b}'.format(plaintext)


if __name__ == '__main__':
    encoded = encode('doubledoubletoilandtroublefireburnandcauldronbubble')
    print(encoded)

    decoded = decode(encoded)
    print(decoded)

    key = generate_key(len(encoded))
    print(key)

    ciphertext = encrypt(encoded, key)
    print(ciphertext)

    plaintext = decrypt(ciphertext, key)
    print(plaintext)

    decoded = decode(plaintext)
    print(decoded)