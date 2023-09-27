# # if statements help our program to behave in ways that we define
# #if statements end in a :
# # < less than   > greater than >= greater and equal to    == euals != not eual to 
# price = float(input('Enter price:'))
# if price >= 10:
#     tax = 0.1
#     print(f'Tax is {tax}')

# #use the else statement to set a defual 

# else:
#     tax = 0
#     print(f'Tax is {tax}')

# #When comparing strings pay attention to cases

# Country = input('Where are you from? ')
# if Country.upper() == 'CANADA':#this makes the input uppercase
#     print('You are Canadian')
# else:
#     print('You are not Canadian')  


    #More than one conditions

# state= input('What is your state? ')


# tax = ''

# if state.upper() == 'ABUJA': # the case format msut match the condition result     
#     tax = 10
# elif state.upper() == 'LAGOS':
#     tax = 20
# elif state.upper() == 'ABIA':
#     tax = 15

# # in / or statements 
# elif state.upper() == 'MINA' or 'NIGER':
#     tax = 4 
# elif state in('ENUGU' , 'IMO' , 'SOKOTO'):
#     tax = 3
# else:
#     tax = 0
# print(f'Your tax is {tax}')

#nested if statents 

# ocupation = input('What do you do? ')

# if ocupation.capitalize() == 'Student':
#    major = input('What is your major? ')

#    if major.capitalize() == 'Medcine':
#        print('you are going to be a doctor')
#    elif major.capitalize == 'Engineering':
#        print('You are going to be an Engineer')
# else:
#     print('You are not a student!')

#using And to combine conditions instead of nesting 
gpa = float(input('Enter GPA: '))
lowest_grade = float(input('Enter GPA: '))

# if gpa >= .85:
#     if lowest_grade >= .70:
#         print('Good job!')

# if gpa >=.85 and lowest_grade >= .07:
#     print('Great Job')


if gpa >=.85 and lowest_grade >= .07:
    honourable = True
else:
    honourable = False

if honourable:
    print('CONGRATULATION')
else:
    print('Carry Over')





