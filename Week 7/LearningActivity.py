# Write a program with three fuctions.
# function 1 prints the strings exactly the way it is recieved 
# function 2 turns to uppercase 
# function 3 turns everything to lowercase 

print()

def print_original(alert):
    message_original = message
    return message_original

def print_upper(alert):
    meaagse_upper = message.upper()
    return meaagse_upper

def print_lower(alert):
    message_lower = message.lower()
    return message_lower

message = input("Type a message: ")
original = print_original(message)
uppercase = print_upper(message)
lowercase = print_lower(message)

print(f"Your message is \n {original} \n {uppercase}\n {lowercase}")
