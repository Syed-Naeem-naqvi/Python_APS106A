# Lec7

# ex1
# v1 = True
# v2 = False
# print(v1, v2)
# s = v1 and v2
# print(s)

# ex2
# a = True and True
# b = True and False
# c = a and not b
# print(c)

# ex3
var1 = True and True  # T
var2 = True and False  # F
var3 = var1 or var2  # F
# print(var3)

# ex4
a = 1 == 2
print(a)

# lazy evaluation: something terrible could happen


def f():
    print('Hi')
    return False


print(True or f())
print(False or f())

# f() doesnt run in first statement
