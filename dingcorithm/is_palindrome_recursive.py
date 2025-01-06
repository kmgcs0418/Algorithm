input = "abcba"


def is_palindrome(string):
    return is_palindrome(string[1:-1])


print(is_palindrome(input))