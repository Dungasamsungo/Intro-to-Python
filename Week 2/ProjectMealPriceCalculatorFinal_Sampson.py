#MEAL PRICE CALCULATOR

#Creativity: I used an if statement calculate and give a 20% discount when ever the subtal is equal or greater than $20
# When the purchase is less than $20 No 0 discount is given.

#prompt the user for the food price
child_meal_price = float(input("What is the price for a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
print()

#prompt user for the number of children and adults
no_of_children = int(input('How many children are there? '))
no_of_adults = int(input('How many adults are there? '))
print()

#find meal cost by multiplying cost by no of people 
child_meal_cost = child_meal_price * no_of_children
adult_meal_cost = adult_meal_price * no_of_adults

subtotal = child_meal_cost + adult_meal_cost

print(f'Subtotal: ${subtotal :.2f}')
print()

#giving a 20% discount for all purchase of $20 and above
if subtotal >= 20:
    discount = subtotal * 20 / 100
elif subtotal < 20:
    discount = 0

#prompt for the sales tax rate
sales_tax_rate = float(input('What is the sales tax rate? '))
print()

#calculate the sales tax by multiflying the subtotal by sales tax rate and dividing the result by 100
sales_tax = (subtotal * sales_tax_rate) / 100
total = (subtotal + sales_tax) - discount 
print(f'Discount: ${discount:.2f}\nSales Tax: ${sales_tax :.2f}\n\nTotal: ${total :.2f}\n')

payment_amount = float(input('What is the payment amount? '))
change = payment_amount - total
print(f'Change: ${change :.2f}')



