# Built in functions: help() and print()
print(help(abs))
print(help(print))
print(3, 5, 'a', sep="+")

print(3, 5, 'a', sep="+", end="22")
print(6, 7)
print('hi')

# 6 and 7 on the same line because end is not the newline character
# can avoid putting output on new line with end

# Want quotation marks?
print('"hi"')

########################

print("Result of 2+5 is", 2+5)

# input()
input_val = input("Give me a temperature in F: ")
print(input_val)


