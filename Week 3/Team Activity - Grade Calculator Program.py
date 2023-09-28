#Team activity 
# GADE CALCULATOR 

#core requirments

# No1
# #Promt user for a grade percentage
# grade_percentage = float(input('Enter grade percentage: '))

# # Use conditions to determine the grade 
# if grade_percentage >= 90:
#     grade = 'A'
#     print(f'Grade is: {grade}')

# elif grade_percentage >= 80:
#      grade = 'B'
#      print(f'Grade is: {grade}')

# elif grade_percentage >= 70:
#      grade = 'C'
#      print(f'Grade is: {grade}')

# elif grade_percentage >= 60:
#      grade = 'D'
#      print(f'Grade is: {grade}')

# else :
#      grade = 'F'
#      print(f'Grade is: {grade}')
# print()

# # No 2

# # Display a congratulatory orencouragement message 

# if grade_percentage >= 70:
#      print('Congratulations! you passed the course.')

# else:
#      print("You are almost there. Don't give up.")

#No 3 

#Promt user for a grade percentage
grade_percentage = float(input('Enter grade percentage: '))

# Use conditions to determine the grade 
if grade_percentage >= 90:
    letter = 'A'
    

elif grade_percentage >= 80:
     letter = 'B'
     

elif grade_percentage >= 70:
     letter = 'C'
    

elif grade_percentage >= 60:
     letter = 'D'
    

else :
     letter = 'F'

print(f'Your garde is: {letter}')
    
print()

# No 2

# Display a congratulatory orencouragement message 

if grade_percentage >= 70:
     print('Congratulations! you passed the course.')

else:
     print("You are almost there. Don't give up.")


# Stretch Challenge 

last_number = grade_percentage%10


if last_number >= 7:
     sign = '+'
     

elif last_number < 3:
     sign = '-'     

else:
     sign = ''



print(f'Your garde is {letter}{sign}')



