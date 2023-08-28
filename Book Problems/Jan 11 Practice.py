# CH 3 Questions
a = min(2, 3, 4)
b = max(2, -3, 4, 7, -5)
c = max(2, -3, min(4, 7), -5)
print(a, b, c)


# Q3-7

def triple(x):
    return x*3


def abs_diff(a, b):
    return abs(a-b)


def conv_miles(km):
    return km/1.6


def mean_of_3(n1, n2, n3):
    avg = (n1 + n2 + n3)/3
    return avg


print(triple(2))
print(mean_of_3(2,3,4))

# Q8


def weeks_elapsed(day1, day2):
    """ (int, int) -> int
    day1 and day2 are days in the same year. Return the number of full weeks that have elapsed between the two days.
    """
    days_per_week = 7
    difference = abs(day1 - day2)
    full_weeks = difference // days_per_week
    return full_weeks


print(weeks_elapsed(3, 20))
print(weeks_elapsed(20, 3))
print(weeks_elapsed(8, 5))
print(weeks_elapsed(40, 61))

# Q9 and 10


def square(x):
    return x**2


print(square(9))

