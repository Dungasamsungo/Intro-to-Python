import random


# core requirements 1 

magic_number =  int(input('What is the magic number? '))
guess =  int(input('What is your guess? '))

if guess == magic_number:
    print('You guessed it!')

elif guess < magic_number:
    print('Higer')
    

else:
    print('Lower')
    


# core requirements 2 

magic_number =  int(input('What is the magic number? '))

while True:
    guess =  int(input('What is your guess? '))
    if guess == magic_number:
        print('You guessed it!')
        break

    elif guess < magic_number:
        print('Higer')

    else:
        print('Lower')
   

# core requirements 3 

magic_number = random.randint(10, 20)

while True:
    guess =  int(input('What is your guess? '))
    if guess == magic_number:
        print('You guessed it!')
        break

    elif guess < magic_number:
        print('Higer')

    else:
        print('Lower')
   


   
         

             


 
     

