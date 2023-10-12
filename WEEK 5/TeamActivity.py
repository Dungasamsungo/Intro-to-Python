#Team Activity - Lists of Numbers


# Core Requirements
# Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0.
# Compute the sum, or total, of the numbers in the list.
# Compute the average of the numbers in the list.
# Find the maximum, or largest, number in the list.

print()
numbers = [] # declare an emty list
new_number = None 

print('Enter a list of numbers, type 0 when finished.')
print()
while new_number != 0: # promt user for a number until 0 is entered 
    new_number = int(input('Enter number: '))

    if new_number != 0: #append all numbers to the numbers list expect 0
        numbers.append(new_number)

total = sum(numbers) # add all the numbers in the list
print()
print(f'The sum is: {total}')
print()


avereage = total / len(numbers) # calculate the average of the numbers in the list

print(f'The sum is: {avereage}')
print()

largest_number = max(numbers) # find the highest or the maximum number in the list

print(f'The largest number is: {largest_number}')
print()



