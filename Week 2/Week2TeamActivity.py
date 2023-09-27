import math
# Week Team Activity

#Area of a square

side = float(input('Enter the lentght of one side of the square:'))
area = side **2

print(f'The area of the square is {area}\n')

#Area of a rectangle 

lenght = float(input('Enter the lenght of the rectangle:'))
width = float(input('Enter the width of the rectangle:'))
Area = lenght * width 

print(f'The area of the rectangle is: {area}\n')

#Area of a circle 

radius = int(input('Enter the radius of the circle:'))
area = math.pi * (radius **2)

print(f'The area of the circle is:{area}')


