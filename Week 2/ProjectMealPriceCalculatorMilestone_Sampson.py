#MEAL PRICE CALCULATOR

#Ask the user for the food price
child_meal_price = float(input("What is the price for a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
print()

#ask user for the number of children and adults
no_of_children = int(input('How many children are there? '))
no_of_adults = int(input('How many adults are there? '))
print()

#find meal cost by multiplying cost by no of people 
child_meal_cost = child_meal_price * no_of_children
adult_meal_cost = adult_meal_price * no_of_adults

subtotal = child_meal_cost + adult_meal_cost

print(f'Subtotal: ${subtotal :.2f}')