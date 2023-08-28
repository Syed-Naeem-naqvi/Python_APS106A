import math as m
# Q1 123 --> 321


def reverse_number(x):

    """  (int) -> (int)
    reverses a number returning a three digit integer
    # first_digit = x % 10
    # second_digit = (x % 100) // 10
    # third_digit = (x % 1000) // 100
    """
    first_digit = x % 10
    second_digit = (x % 100) // 10
    third_digit = (x % 1000) // 100
    output_num = str(first_digit) + str(second_digit) + str(third_digit)
    return output_num


# print(reverse_number(789))

# Q2

def make_change(amt):
    """
    returns the number of pennies, nickels, dimes and quarters that make up the change
    """
    q = amt // 25
    amt -= (25*q)
    d = amt // 10
    amt -= (10*d)
    n = amt // 5
    amt -= (5*n)
    p = amt // 1
    amt -= (1*p)
    return p, n, d, q


# print(make_change(67))

# Q3

f = float(input('Enter a float: '))
f1 = m.trunc(f*10)/10
f2 = round(f, 1)
# print(f1, f2)

# Q4


def trig_calc(x):
    sin = round(m.sin(x * m.pi / 180), 5)
    cos = round(m.cos(x * m.pi / 180), 5)
    tan = round(m.tan(x * m.pi / 180), 5)
    return_statement = (sin, cos, tan)
    return return_statement


# print(trig_calc(60))

# Q5


def clerk(cost, paid):
    change = 0
    required_amount = 0
    if cost < paid:
        change = paid - cost
        return_statement = 'Your change is: $' + str(change)
    elif cost > paid:
        required_amount = cost - paid
        return_statement = 'You owe: $' + str(required_amount)
    else:
        return_statement = "You are set"
    return return_statement


# print(clerk(10.00, 13.00))

# Q6

def clerk_v2(cost, paid):
    change = 0
    required_amount = 0
    if cost < paid:
        returned_change = round((paid - cost), 2)
        change = round((paid - cost), 2)
        hundreds_ = change // 100
        change -= (100 * hundreds_)

        fifties_ = change // 50
        change -= (50 * fifties_)

        twenties_ = change // 20
        change -= (20 * twenties_)

        tens_ = change // 10
        change -= (10 * tens_)

        fives_ = change // 5
        change -= (5 * fives_)

        twos_ = change // 2
        change -= (2 * twos_)

        ones_ = change // 1
        change -= ones_

        quarters_ = change // 0.25
        change -= (0.25 * quarters_)

        dimes_ = change // 0.10
        change -= (0.10 * dimes_)

        nickels_ = change // 0.05
        change -= (0.05 * nickels_)

        pennies_ = change // 0.01
        change -= (0.01 * pennies_)

        return_statement = (returned_change, hundreds_, fives_, twenties_, tens_, fives_, twos_, ones_, quarters_, dimes_, nickels_, pennies_)
    elif cost > paid:
        required_amount = cost - paid
        return_statement = 'You owe: $' + str(required_amount)
    else:
        return_statement = "You are set"
    return return_statement


# print(clerk_v2(5, 5.01))

# Q7

def clerk_v3(cost, paid):
    change = 0
    required_amount = 0
    if cost < paid:
        returned_change = round((paid - cost), 2)
        change = round((paid - cost), 2)
        hundreds_ = change // 100
        change -= (100 * hundreds_)

        fifties_ = change // 50
        change -= (50 * fifties_)

        twenties_ = change // 20
        change -= (20 * twenties_)

        tens_ = change // 10
        change -= (10 * tens_)

        fives_ = change // 5
        change -= (5 * fives_)

        twos_ = change // 2
        change -= (2 * twos_)

        ones_ = change // 1
        change -= ones_

        quarters_ = change // 0.25
        change -= (0.25 * quarters_)

        dimes_ = change // 0.10
        change -= (0.10 * dimes_)

        nickels_ = change // 0.05
        change -= (0.05 * nickels_)

        pennies_ = change // 0.01
        change -= (0.01 * pennies_)

        if pennies_ < 3:
            pennies_ = 0
        elif pennies_ >= 3:
            pennies_ = 0
            nickels_ += 1

        return_statement = (returned_change, hundreds_, fifties_, twenties_, tens_, fives_, twos_, ones_, quarters_, dimes_, nickels_, pennies_)
    elif cost > paid:
        required_amount = cost - paid
        return_statement = 'You owe: $' + str(required_amount)
    else:
        return_statement = "You are set"
    return return_statement


# print(clerk_v3(5, 10.01))

# Q8


def count_digits():
    """ (int) -> (int)
    returns the number of digits in a number x
    less than 100,000
    """
    digits = 0
    x = int(input('Enter: '))
    if x < 100000 and x != 0:
        ten_thousands = x // 10000
        if ten_thousands != 0:
            digits += 1
        thousands = x // 1000
        if thousands != 0:
            digits += 1
        hundreds = x // 100
        if hundreds != 0:
            digits += 1
        tens = x // 10
        if tens != 0:
            digits += 1
        ones = x // 1
        if ones != 0:
            digits += 1
    elif x == 0:
        digits = 1
    else:
        print('Invalid number')
        digits = 'Error'
    return digits

print(count_digits())


def count_digits_v2():
    x = input('Enter an integer: ')
    x_int = int(x)
    if x_int < 100000:
        return x.__len__()
    else:
        print('INVALID')


# print(count_digits_v2())


# Q9


def determine_state():
    """ (int) -> 'string'
    Given the temperature T in celsius, determines the
    physical state of water
    """

    T = int(input("Enter the water temperature in celsius: "))
    if T >= 100:
        statement = 'Gas'
    elif 0 < T < 100:
        statement = 'Liquid'
    elif -273 < T <= 0:
        statement = 'Solid'
    else:
        statement = 'INVALID INPUT, SELF DESTRUCTING IN 10 SECONDS'

    return statement


print(determine_state())

# Q10


