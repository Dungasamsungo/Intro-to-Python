#Word Puzzle

# I created a list of words and the program randomly selects one every time it runs


import random # imports the random libary 


word_list = ['sampson', 'john', 'book']
word = random.choice(word_list) # makes a random sellection of a word from the word_list variable. 
print()
print('*********************************')
print('WELCOME TO THE WORD GUESS PUZZLE')
print()
print(f'Your hint is: ', end='')

count = 0
while count < len(word): #Displays an initial hint 
  
    print(f'_', end=' ')
    count += 1
print()
print()
guess = input('What is your guess? ').lower() #Promt user for a guess and covert it to lowercase

attempts = 1
while guess != word:
    attempts += 1
    
    if len(guess) != len(word): # Check if the lenght of guess is same as word lenght
        print()
        print('Sorry, the guess must have the same number of letters as the secret word.')   
        
    else:# update hint
        count = 0
        print('Your hint is: ', end=' ')
        while count < len(guess):
            
            if guess[count].lower() not in word:# print an underscore when guess is not in word
                print('_', end=' ')
                                    
            elif guess[count].lower() == word[count]: # the guessed letter is printed in uppercase if it's in word and at the right position
                print(guess[count].upper(), end=' ')
                                    
            else:
                print(guess[count].lower(), end=' ') #if guessed letter is in word but in a different location, it is printed in lowercase
            count = count + 1
             
    print()                       
    guess = input('What is your guess? ').lower()
    print()

else: # print a congratulary message and the number of guesses when the quess is quals to the word
    if guess.lower() == word.lower():
        print()
        print('Congtratulations!. You guessed it!')
        print(f'It took you {attempts} guess(es).')
        print()
        print('*********************************')


            
   
   
       