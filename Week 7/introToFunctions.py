from datetime import datetime

# Print timestamps to see how long sections of my code takes to run

# first_name = "sampson"
# print("task completed")
# print(datetime.datetime.now())
# print()

# for x in range(0,11):
#     print(x)
# print("task completed")
# print(datetime.datetime.now())
# print()


# # The repeated code can be put in a function 

# def print_time(): # prints timestamp everytime you call it
#     print("task completed")
#     print(datetime.datetime.now())
#     print()

# first_name = "sampson"
# print_time()

# for x in range(0,11):
#     print(x)
# print_time()

# Everytime I want to change something or add something new the time code
# I need to change only the function and everything becomes ok

# Let's change the import of the time lib and call it differently 

# def print_time(): # prints timestamp everytime you call it
#     print("task completed")
#     print(datetime.now())
#     print()

# first_name = "sampson"
# print_time()

# for x in range(0,11):
#     print(x)
# print_time()

# We can also pass parameters to the function 

# def print_time(task_name): # prints timestamp everytime you call it
#     print(task_name) # remember to pass your parameter here
#     print(datetime.now())
#     print()

# first_name = "sampson"
# print_time("Printed first name")

# for x in range(0,11):
#     print(x)
# print_time("for loop completed")

#EXAMPLE 2

# Ask for users names and return their initials
 
#WITHOUT FUNCTION
first_name = input("Enter your first name: ").upper()
first_name_initial = first_name[0:1]

middle_name = input("Enter your middle name: ").upper()
middle_name_initial = middle_name[0:1]

last_name = input("Enter your Last name: ").upper()
last_name_initial = last_name[0:1]

print(f"Your initials are {first_name_initial}{middle_name_initial}{last_name_initial}")

# WITH FUNCTION 

# This function returns the initials of the names 
def get_initials(name):
    initial = name[0:1].upper()
    return initial

first_name = input("Enter your first name: ")
first_name_initial = get_initials(first_name)

middle_name = input("Enter your middle name: ")
middle_name_initial = get_initials(middle_name)

last_name = input("Enter your Last name: ")
last_name_initial = get_initials(last_name)

print(f"Your initials are {first_name_initial}{middle_name_initial}{last_name_initial}")
