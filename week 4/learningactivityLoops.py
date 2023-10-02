#Loops


tip = float(input('Enter the amount: ')) #declare veriables before the if or loop statements 

if tip < 0:  # this does not fix our problem. after the first attempt it will print the negative amount.
    print('You cannot tip negative amounts. Enter a valid tip ')
    tip = float(input('Enter the amount: ')) 

while tip < 0:  # this solves the problem by testing the number every time until the value changes
    print('You cannot tip negative amounts. Enter a valid tip ')
    tip = float(input('Enter the amount: ')) 




print(f'You have tipped ${tip:.2f}')