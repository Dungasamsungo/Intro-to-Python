#Word Puzzle
# Mile stone

import random # imports the random libary 


word_list = ['sampson', 'john', 'book']
word = random.choice(word_list) # makes a random sellection of a word from the word_list variable. 
print()
print('*********************************')
print('WELCOME TO THE WORD GUESS PUZZLE')
print()
print(f'Your hint is: ', end='')

count = 0
while count < len(word):
  
    print(f'_', end=' ')
    count += 1
print()
print()
guess = input('What is your guess? ').lower()

attempts = 1
while guess != word:
    attempts += 1
    
    if len(guess) != len(word):
        print()
        print('Sorry, the guess must have the same number of letters as the secret word.')   
        
    else:
        count = 0
        print('Your hint is: ', end=' ')
        while count < len(guess):
            
            if guess[count].lower() not in word:
                print('_', end=' ')
                                    
            elif guess[count].lower() == word[count]:
                print(guess[count].upper(), end=' ')
                                    
            else:
                print(guess[count].lower(), end=' ')
            count = count + 1
             
    print()                       
    guess = input('What is your guess? ').lower()
    print()

else:
    if guess.lower() == word.lower():
        print()
        print('Congtratulations!. You guessed it!')
        print(f'It took you {attempts} guess(es).')
        print()
        print('*********************************')


            
   
   
       