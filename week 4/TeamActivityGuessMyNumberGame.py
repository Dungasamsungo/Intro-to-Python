import random



magic_number =  int(input('What is the magic number? '))
guess =  int(input('What is your guess? '))

if guess == magic_number:
    print('You guessed it!')

elif guess > magic_number:
    print('Lower')

else:
     print('Higer')


