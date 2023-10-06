#Word Puzzle
# Mile stone

Secret_word = 'samson'
print()
guess = input('What is your guess? ')

attempts = 0

while True:
    attempts += 1

    if guess.lower() == Secret_word:
        print()
        print('Congtratulations!. You guessed it!')
        print(f'It took you {attempts} guesses.')
        break
    else: 
        print()
        print('Your guess was not correct!')
        guess = input('What is your guess? ')
        print()
   
       