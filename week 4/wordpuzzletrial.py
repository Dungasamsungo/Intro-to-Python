import random

word_list = ['sampson', 'john', 'book']
word = random.choice(word_list)

# Initialize variables
attempts = 0
guessed_word = ["_"] * len(word)

print("Welcome to the word guessing game!")
print("Your hint is:", " ".join(guessed_word))

while True:
    guess = input("What is your guess? ")

    attempts += 1

    if guess.lower() == word.lower():
        print()
        print('Congratulations! You guessed it!')
        print(f'It took you {attempts} guesses.')
        break

    if len(guess) != len(word):
        print('Sorry, the guess must have the same number of letters as the secret word.')

    else:
        updated_hint = list(guessed_word)  # Create a copy of the guessed word

        for i in range(len(word)):
            if guess[count].lower() not in word:
                print('Your hint is: ', end='')
                print('_', end='')
                                    
            elif guess[count].lower() == word[count]:
                print(guess[count].upper(), end='')
                                    
            else:
                print(guess[count].lower(), end='')
            count = count + 1
            guess = input('What is your guess? ')

        guessed_word = updated_hint  # Update guessed_word with the new hint
        print("Your hint is:", " ".join(guessed_word))
