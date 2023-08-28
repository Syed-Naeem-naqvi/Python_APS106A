def count_digits(x):
    """ (int) -> int
    Returns the number of digits in an integer
    """
    count = 0
    while x > 0:
        count += 1
        x //= 10
    return count


print(count_digits(199999))


def invert_number(x):

    """ (int) -> int
    Inverts a number
    """

    inverted_number = 0
    while x > 0:
        ones_digit = x % 10
        inverted_number = inverted_number*10 + ones_digit
        x //= 10
    return inverted_number


print(invert_number(12345))


