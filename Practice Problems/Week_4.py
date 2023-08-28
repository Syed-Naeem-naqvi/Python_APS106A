# Q1

def count_digits():
    """ (int) -> (int)
    Prompts the user for a number and counts the number of
    digits
    """
    integer = input("Enter an Integer: ")
    digits = 0
    for i in integer:
        digits += 1
    return digits


# print(count_digits())

# Q2


# Q3
def add_odd_series(odd):
    """ (int) -> (int)
    Given an odd number, returns the sum of the
    series consisting of odd numbers starting at 1
    up to odd.
    """
    _sum = 0
    while odd >= 1:
        _sum += odd
        odd -= 2
    return _sum


# odd_ = int(input('Enter odd number: '))
# while odd_ < 0 or odd_ % 2 == 0:
#     odd_ = int(input("Enter odd number: "))

# print(add_odd_series(odd_))


# Q4

def count_positives_and_negatives():
    """ (user input) -> (positives, negatives)
    Counts the number of positive and negative numbers the user enters
    and returns the counts when a zero is entered
    """
    positives = 0
    negatives = 0
    user_number = int(input('Enter an integer: '))
    while user_number != 0:
        if user_number > 0:
            positives += 1
        elif user_number < 0:
            negatives += 1
        user_number = int(input('Enter an integer: '))

    return positives, negatives


# print(count_positives_and_negatives())
