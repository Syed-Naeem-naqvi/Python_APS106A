
def estimate_inv_hyperbolic_tan(x, ε):
    """ (float, float) -> (float)

    Given some |x| < 1 and some small  ε > 0, return
    the value of the series representation of hyperbolic tan-1(x) using
    a number of terms such that the difference from adding a new
    term would be less than or equal to ε

    """

    estimate = 0
    next_estimate = 0
    current_term = 0

    for i in range(1, 1001, 2):
        current_term = i
        next_estimate += (x ** i) / i
        estimate = next_estimate - (x ** current_term) / current_term
        diff = next_estimate - estimate
        if diff < ε:
            break

    return estimate


y = float(input('Enter a value: '))
while y > 1 or y < -1:
    y = float(input('Enter a value: '))

ε = 0.001
print(estimate_inv_hyperbolic_tan(y, ε))







