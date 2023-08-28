x = 0.5
estimate = 0
next_estimate = 0
current_term = 0
ε = 0


for i in range(1, 41, 2):
    current_term = i
    next_estimate += (x**i)/i
    estimate = next_estimate - (x**current_term)/current_term
    ε = next_estimate - estimate
    print(next_estimate, estimate, current_term, ε)
    if ε < 0.001:
        break
        print(ε, estimate)


print(estimate)

