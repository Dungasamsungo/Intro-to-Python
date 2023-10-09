# #Loops


# # tip = float(input('Enter the amount: ')) #declare veriables before the if or loop statements 

# # if tip < 0:  # this does not fix our problem. after the first attempt it will print the negative amount.
# #     print('You cannot tip negative amounts. Enter a valid tip ')
# #     tip = float(input('Enter the amount: ')) 

# # while tip < 0:  # this solves the problem by testing the number every time until the value changes
# #     print('You cannot tip negative amounts. Enter a valid tip ')
# #     tip = float(input('Enter the amount: ')) 


# #print(f'You have tipped ${tip:.2f}')

# # word count with loops 

# # number = 1

# # while number <= 5:
# #     print(f'The number is = {number} ')
# #     number = number + 1

# # number = 0

# # while number < 10:
# #     number = int(input(' What is the number? '))


# #activity



# # number = int(input('Please type a positive number: '))

# # while number < 0:
# #      print("Sorry that's a negative number. Please try again")
# #      number = int(input('Please type a positive number: '))

# # print(f'the number is: {number}')
# # print()


# # response = ''

# # while response == 'no':
# #     response = input('May I have a Candy? ')

# # print('Thank You ')

# # answer = input("May I have a piece of candy? ")

# # while answer != "yes":
   
# #     answer = input("May I have a piece of candy? ")

# # print ("Thank you.")
# # # # number  =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # # print(number)
# # # # print()

# # # # number = range(10)
# # # # print(number)

# # # # print()

# # # # for number in range(11):
# # # #     print(number)

# # # # for i in range(100, 201):
# # # #     print(i)

# # for i in range(10, 100, 10):
# #     print(i)

# # for i in range (1,11):
# #     print(i)
# #     for c in range (2,10,2):
# #         print(f'-{c}')


# # colors = ["red", "blue", "green", "yellow"]

# # for color in colors:
# #     print(color)
# #     print()



# # for i in range (1,9):
# #     print(i)
# #     print()

# # for i in range (2,22,2):
# #     print(i)

# # name = 'Sampson'
# # for letter in name:
# #     print(f'The letteris: {letter}')

# # name = 'Ngobi'
# # second_letter = name[1]
# # print(second_letter)
# # print()

# # word = 'laptop'
# # number_ofletters = 6

# # for index in range (number_ofletters):
# #     print(index)
    

# # word = 'laptop'
# # number_ofletters = 6

# # for index in range (number_ofletters):
# #     letter = word[index]
# #     print(f'Index: {index} Letter: {letter}')

# # first_name = input("WHat's your first name? ")
# # letter_count = len(first_name)

# # print(f'Your first name has {letter_count} letters')

# # first_name = input("What's your first name? ")

# # # Notice by using enumerate, we specify both i and letter
# # for i, letter in enumerate(first_name):
# #     print(f"The letter {letter} is at position {i}")
    

# animal = "rabbit"
# while animal == "dog":
#    print("a")
#    animal = "cat"
#    print("b")
# print("c")
# print()

# animal = "dog"
# while animal == "dog":
#    print("a")
#    animal = "cat"
#    print("b")
# print("c")
# print()

# animal = "dog"
# while animal != "dog":
#    print("a")
#    animal = "cat"
#    print("b")
# print("c")
# print()

# value = 10
# while value < 20:
#    value = value + 1
# print(value)
# print()

# while value < 20:
#    value = value + 1
# print(value)
# print()

# value = 20
# while value < 20:
#    value = value + 1
# print(value)
# print()

# while value < 20:
#    value = value + 1
# print(value)
# print()

# while value < 20:
#    value = value + 1
# print(value)

# Promt for a positive number 
number = int(input('Please type a positive number: '))
# loop for as long as the number is not positive. That is numbers >= 0
while number < 0:
    print('Sorry that is a negative number!')
    number = int(input('Please type a positive number: '))
    
# print the positive number 
else:
    print(f'The number is {number}')



print() # A child ask the parents for a piece of candy. 
response = input('May I have a piece of candy? ')# Parents enters a response 

while response.lower() != 'yes': # Loop to repeat the questions until the answer is yes 
    response = input('May I have a piece of candy? ')

else:
    print('Thank you') # print thank you


#teachers way

print() # A child ask the parents for a piece of candy. 
response = ''# declare the response veriable and assign a string to allow it enter loop

while response.lower() != 'yes': # Loop to repeat the questions until the answer is yes 
    response = input('May I have a piece of candy? ')


print('Thank you') # print thank you



