from exercises.fundamentals.src.palindrome import palindrome


def test_palindrome():
    is_palindrome = palindrome('dad')
    assert is_palindrome

    is_palindrome = palindrome('cat')
    assert not is_palindrome

    is_palindrome = palindrome('racecar')
    assert is_palindrome

    is_palindrome = palindrome('purple')
    assert not is_palindrome

    is_palindrome = palindrome('civic')
    assert is_palindrome
