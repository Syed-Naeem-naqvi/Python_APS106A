import random as r
# Lecture example


secret_number = r.randint(0, 100)
guess = input('Guess the number: ')

while guess != 'n':

    if int(guess) > secret_number:
        print('Guess lower')
        guess = input('Guess the number: ')

    elif int(guess) < secret_number:
        print('Guess Higher')
        guess = input('Guess the number: ')

    elif int(guess) == int(guess):
        print("You Win")
        break

else:
    print("Game Over")

