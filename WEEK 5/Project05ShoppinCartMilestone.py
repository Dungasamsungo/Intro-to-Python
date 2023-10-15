# To show creativity, I use the try and except function to reject string 
#inputs and numbers less than 0 or greater than 5

print()
print('WELCOME TO THE CART PROGRAM!')

print()

# Declare the list varables to be empty 
cart = []
prices = []

# lope a promt for an inpute until the user types in 5 to quit
number = 0
while number != 5:
    try:
        
        print('Please enter a number from the menu: ') # this displays the options 
        print()
        print('1. Add item')
        print('2. View cart')    
        print('3. Remove item')
        print('4. Compute total')
        print('5. Quit')
        
        number =int(input('Please enter an action: ')) # Prompt for action 
        print()

        # add items and prices to the lists 
        if number == 1:
            new_item = input('What item would you like to add? ')
            cart.append(new_item)
            print()
        
            price = float(input(f'What is the price of {new_item}: '))
            prices.append(price)
            print()
            print(f'{new_item} has been added to the cart.')
            print()
                
        # Display the cart and prices 
        elif number == 2:
            print('The content of the shopping cart is: ')
            count = 0
            for i in range(len(cart)):
                print(f'{count + 1}. {cart[i]} - ${prices[i]:.2f}') 
                count += 1    
            print()

        # Remove an item and print the remaining content of the cart
        elif number == 3:
            count = 0
            while count < len(cart):
            
                delete_index = int(input('What item do you want to remove? '))
                delete_index = delete_index = 1
                cart.pop(delete_index)
                prices.pop(delete_index)
                print('Item has been removed')
                print()

                count = 0
                print(f'Cart content is now: ')
                while count < len(cart):
                    print(f'{count + 1}. {cart[count]} - ${prices[count]:.2f}')
                    count += 1
                print()

            
        # calculate the sum of the prices 
        elif number == 4:
            total = sum(prices)
            print(f'The total price of all items in the cart is: ${total:.2f}')
            print()

        # Quit the program
        else:
            if number == 5:
                print('Thank you and Goodbye')
                print()
                break
    
    except:
        print('Enter only numbers from 0 to 5')
        print()

    

    

       

    

    



    


