# Stop: PR - 28

# Guess the number

import random

print("Hi! Guess the number and enter your name!"); print()
number = random.randint(1, 100)


name = input("Enter your name: ").strip().capitalize()

while True:
    try:

        guess = int(input('Guess the number, please: '))

        if guess == number:
            print(f'Hooray you guessed the game! The answer: {number}')
            False
        elif guess > number:
            print('Too big');
        elif guess < number:
            print('Too small');
        else:
            print('Invalid syntax')

    except ValueError:
        print('Invalid input, please enter a number again.')
        continue



    print('Do you want to surrender?'); surrender = input('yes/no: ');
    if surrender in [ 'yes', 'ye', 'y']:
        print(f'The answer was: {number}');
        break
    elif surrender in [ 'no', 'n']:
        print(f'Good luck, user {name}');
    else:
        print('Invalid syntax. Please respond with \'yes\' or \'no\'.')
    print('You can do this!')

print(f'Thanks for playing, user {name}!\n\tMade by Sneoklid and VISE')