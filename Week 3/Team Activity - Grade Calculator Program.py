#Team activity 
# GADE CALCULATOR 

#core requirments

# 1
grade_percentage = float(input('Enter grade percentage: '))

if grade_percentage >= 90:
    grade = 'A'
    print(f'Grade is: {grade}')

elif grade_percentage >= 80:
     grade = 'B'
     print(f'Grade is: {grade}')

elif grade_percentage >= 70:
     grade = 'C'
     print(f'Grade is: {grade}')

elif grade_percentage >= 60:
     grade = 'D'
     print(f'Grade is: {grade}')

else :
     grade = 'F'
     print(f'Grade is: {grade}')
