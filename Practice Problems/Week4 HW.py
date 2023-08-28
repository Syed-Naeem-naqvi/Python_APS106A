import random as r

k = r.randint(0, 100)

q = int(input('Enter your guess: '))
while q != k:
    if k > q:
        print('Guess higher')
        q = int(input('Enter your guess: '))
    else:
        print('Guess lower')
        q = int(input('Enter your guess: '))
else:
    print("You did it! Here's a cookie")




