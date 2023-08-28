def conv_to_c(f):
    """ (number) -> (number)
    Translates f to c
    """
    c = (f - 32) * 5/9
    return c


print(conv_to_c(212))
# print(c) c is a local variable, only visible in function

returned_by_function = conv_to_c(212)  # Now we've defined it outside too
print(returned_by_function)

# Cant use print(c) instead of return c because the function call will return none





