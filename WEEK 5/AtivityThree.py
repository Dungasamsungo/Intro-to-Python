print()

# Ask the user for a list of items in a shopping list, stop asking for items when the user types "quit."
shopping_list = []
item = None

print('Please enter the items of the shopping list (type: quit to finish):')

while item != 'quit':
   item = input('Item: ').lower()

   if item != 'quit':
      shopping_list.append(item)


# Loop through the items in the regular way (for example, for thing in the_list) and display 
# each one to make sure you have the initial list built correctly.
print()
print('The shopping List is:')

for item in shopping_list:
   print(item)

# Add another loop to go through and print the items in the list, but this time, 
# instead of using the for ... in syntax, use an index (for example, for ... in range) and 
# then access the item using the index and the square brackets. Print the index in front of the items like so: 0. Milk
print()
print('The shopping list with index is:')

for i in range(len(shopping_list)): 
   item = shopping_list[i]
   print(f'{i + 1}. {item}')
   
# Ask the user for an index and a new shopping list item. Replace the item at that index with the new item. Then, display the whole list again.

print()
index = int(input('What item do you want to remove? '))
new_item = input('What is the new item: ')

shopping_list[index] = new_item

print('The shopping list with index is:')
    
for i in range(len(shopping_list)): 
   item = shopping_list[i]
   print(f'{i + 1}. {item}')

