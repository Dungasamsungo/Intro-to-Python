#This displays request instruction to the the user
print('Please enter the follow:')
#This gives space between lines
print()

#The user types in the requested information through the input tag
adjective = input('Adjective:')
animal = input('Animal:')
verb = input('Verb:')
exclamation = input('Exclamation:')
verb_2 =input('Verb:')
verb_3 = input('Verb:')
print()
print('Your story is:\n')
#The \n tag takes us to the next line
#The print(f'{}) tag makes it possible to add space and puntuations properly while using data stored in variables
#The .lower() tag keeps the user input in the lower case format, despite the original inpute format
# The .capitalize() makes the first Letter of the word upper case. 
print('The other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. "{exclamation.capitalize()}!" I yelled. But all')
print(f'I could think to do was to {verb_2.lower()} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb_3.lower()}')
print(f'right in front of my family.')
print('')
