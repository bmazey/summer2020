

def palindrome(word):

    new_word = ''

    for i in range(len(word)):
        new_word += word[len(word) - 1 - i]

    return new_word == word
