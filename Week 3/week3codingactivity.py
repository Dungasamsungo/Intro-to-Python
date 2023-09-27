print('For each of these questions, enter a value between 1 and 10')
print()

approved = False

loan_size = int(input('How large is the loan? '))
creadit_history = int(input('How good is your creadit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))
print()

if loan_size >= 5:
    if creadit_history >= 7 and income >= 7:
        approved = True
    elif creadit_history >= 7 and income >= 7:
        if down_payment >= 5:
            approved = True
        else:
            approved = False
    else:
        approved = False

else:
    if creadit_history < 4:
        approved = False
    else:
        if income >= 7 and down_payment >= 7:
            approved = True
        elif income >= 4 and down_payment >= 4:
            approved = True
        else:
            approved = False

if approved:
    print('Loan Approved')
else:
    print('Loan is not approved')
