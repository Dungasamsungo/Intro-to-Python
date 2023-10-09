# import random


# # core requirements 1 

# # magic_number =  int(input('What is the magic number? '))
# # guess =  int(input('What is your guess? '))

# # if guess == magic_number:
# #     print('You guessed it!')

# # elif guess < magic_number:
# #     print('Higher')
    

# # else:
# #     print('Lower')
    


# # core requirements 2 

# # magic_number =  int(input('What is the magic number? '))

# # while True:
# #     guess =  int(input('What is your guess? '))
# #     if guess == magic_number:
# #         print('You guessed it!')
# #         break

# #     elif guess < magic_number:
# #         print('Higer')

# #     else:
# #         print('Lower')
   

# # core requirements 3 

# magic_number = random.randint(10, 20) # the programme generates a random number

# while True: # loop through and test the guess
#     guess =  int(input('What is your guess? ')) # the user provides a guess

#     # test the conditions 
#     if guess == magic_number: 
#         print('You guessed it!')
#         break # stops the loop if the guess is = the magic number 

#     elif guess < magic_number: # test the guess and hints to enter a higher number 
#         print('Higer') 

#     else: # test the guess and hints to enter a lower number 
#         print('Lower')
   


   
         
#For loop
print()
# names = ['Sampson, Ngobi']

# # for name in (names):
# #     print(name)

# name = 0
# while name < len(names):
#     print(names [name])
#     name =+ 1


# items = ['pencil', 'pen', 'book', 'earaser']

# for item in (items):
    
#     print(f' This item is: {item}')
    

# for loop with numbers 

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] - # you can declear your numbers variable like this. but this becomes a problem when you have too many numbers.

#numbers = range(11) # Here is a better way to declare your variable 

#for number in range(11): # this does the same thing
#for number in range(1, 21,): # loop starts fron the first to the last number 
#for number in range(1, 21, 3):# counts in the sequence of the third number
    #print(number)

# looping through strings 

#first_name = ('Sampson')
# forth_letter = first_name[3]

# for letter in(first_name):
#     print(f'The forth letter is: {forth_letter}')
# number_of_letters = len(first_name)
# for index in range(number_of_letters):
#     letter = first_name[index]
#     #print(f'Index: {index} letter: {letter}', end='')
# #print(f'number of letters is: {number_of_letters}')
#     print(letter, end='')

#ask for their favourite letter 
#loop through a word 
#If the letter in word is users favourite
# print it out as a capital letter 
# hide it 
#if thw letter in word is not userd favourite
#print as small letter
favorite_letter = input('Enter your favourite letter: ')
word = ('Sampson')
#word_lenght = len(word)

for letter in (word):
   
    if letter.lower() == favorite_letter.lower():

        print(letter.upper(), end='')
    else:
        print(letter.lower(), end='')
for letter in(word):
    if letter.lower() == favorite_letter.lower():
        print('_', end='')


print()         




 
     

