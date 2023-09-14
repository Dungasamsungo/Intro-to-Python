#This gives the user instruction
print('Please enter the following information')
print()

#Basic information
first_name = input('First name:')
last_name = input('Last name:')
email_address = input('Email address:')
phone_number = input('Phone number:')
job_title = input('Job title:')
id_number = input('ID Number:') 

# This is the information for the stretch challenge
hair_color= input('Hair color:')
eyes_color= input('Eyes_color:')
month= input('Month:')
Training= input('Are you on trianing?:')

#print out the ID card
print() 
print('The ID Card is:\n--------------------------------------')
print(f'{last_name.upper()}, {first_name.capitalize()}')
print(f'{job_title.title()}')
print(f'{id_number}')
print()
print(f'{email_address.lower()}\n{phone_number}')
print()
print(f'Hair: {hair_color:15} Eyes: {eyes_color}')
print(f'Month: {month:14} Training: {Training}')

print('--------------------------------------')