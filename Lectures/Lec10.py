count = 1
while count < 11:
    print(count)
    count += 1


cond = input('Wanna convert? (yes/no): ')
while cond != 'no':
    t_f = float(input("Enter t temp: "))
    t_c = (t_f - 32)*5/9

    if t_c > 0:
        print(t_c)

    cond = input('Wanna convert? (yes/no): ')





