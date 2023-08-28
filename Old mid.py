def sum_cubes(n):
    i = 1
    sum_ = 0
    while i <= n:
        sum_ += i**3
        i += 1
    return sum_


print(sum_cubes(2))


def sum_cubes_num_terms(k):
    n = 0
    sum__ = 0
    while sum__ < k:
        sum__ += n**3
        n += 1
    return n-1


print(sum_cubes_num_terms(9))


def moving_average(measurements):
    i = 0
    averages = []
    while i < (len(measurements)-2):
        averages.append((measurements[i] + measurements[i+1] + measurements[i+2])/3)
        i += 1
    return averages


print(moving_average([1, 2, 3, 4, 5]))


def match(pattern, text):
    pass








