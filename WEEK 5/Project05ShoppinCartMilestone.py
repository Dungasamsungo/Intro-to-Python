# # Milestones

# Milestone Requirements
# Have menu system that repeats until the user chooses quit.
# Create a list that will store the names of the items in the shopping cart.
# Complete the option to add the name of the item to the list.
# Complete the option to display the names of the items in the list.

print()
print('WELCOME TO THE CART PROGRAM!')


print()



cart = []
prices = []

number = 0
while number != 5:
    print('Please enter a number from the menu: ')
    print()
    print('1. Add item')
    print('2. View cart')    
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    
    number = int(input('Please enter an action: '))
    print()

    if number == 1:
        new_item = input('What item would you like to add? ')
        cart.append(new_item)
        print()
       
        price = float(input(f'What is the price of {new_item}: '))
        prices.append(price)
        print()
        print(f'{new_item} has been added to the cart.')
        print()
            

    elif number == 2:
        print('The content of the shopping cart is: ')
        count = 0
        for item in cart:
            print(f'{count + 1}. {item} - ${price :.2f}')
            count += 1
           
        print()


    else:
        if number == 5:
            print('Thank you and Goodbye')
            print()
            break

    

    

       

    

    



    


