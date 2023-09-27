
# Numbers can be stored as:
#Integers (whole numbers)
#Float (decimals)
#Strings

#Maths Opperations
# + add          -  subtraction 
# / didvision    *  multiplication
# ** Exponent


# strings are stored with quotes 
# Age = '35'    -  35 is a string
# Age = 35      -  35 is an integer 
num_1 = 4
num_2 = 6

#simple maths opperation 
#print(num_1 + num_2)


#combination of numbers and strings

age = 35
sept = 30
#This will give an error (TypeError: can only concatenate str (not "int") to str)
#print('You are' + age  )

#To aviod this you need to convert the int to string using the str function str(int)
#I can't find how to add a space between are and 35
#finally found that the '' must have space between them for the space.
#print('You are'+' '+ str(age)+' '+'years old' )

# Adding numbers that are stored as strings requires conversion to int
# this is common when you use the input function to ask for numbers 

food = input('food:')
rent = input('rent:')

#print(food + rent)
# if the user inputed 10 and 20 repectively. you will have 1020 when you run your code.

print(int{food} + {rent})




#print(f'You are {age} years old.')
