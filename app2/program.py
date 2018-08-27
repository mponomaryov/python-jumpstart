import random

print('------------------------')
print(' GUESS THAT NUMBER GAME ')
print('------------------------')
print()

the_number = random.randint(0, 100)

while True:
    guess = int(input('Guess a number between 0 and 100: '))
    if guess < the_number:
        print('Too low')
    elif guess > the_number:
        print('Too high')
    else:
        print('You win!')
        break

print('Done.')
