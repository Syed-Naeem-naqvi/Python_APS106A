import math

s = 'Hello'
# print(s)
# print(s[2])

# Wanna cause a runtime error?
# print(s[22])

# Syntactically, Logically and semantically correct
# But causes runtime error

# ep = int(input("Enter: "))
# print(ep*2)


def f():
    x = 1
    return x


# print(f())

# ex1

def rect_area(l, w):
    """  (length, width) -> (area)

    Given length and width, calculates the
    area of a rectangle

    """
    area = l * w
    return area


print(rect_area(1/3, math.pi))

# area is local
# print(area)


def rect_area2(l, w):
    """  (length, width) -> (area)

    Given length and width, calculates the
    area of a rectangle

    """
    area = l * w
    print(area)


# puts out 6 (from function print statement), then none (from missing return), the function doesnt return anything

# practice

