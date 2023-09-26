#import math Library
import math

#Calculating the area of a square
#Declaring variables and asking for a value
sq_length = float(input("What is the length of a side of the square? "))
#The area is the lenght of a side squared
square_area = sq_length**2
#printing results
print(f'The area of the square is: {square_area}')


#Calculating the area of a rectangle
#Declaring variables and asking for a value
re_length = float(input("What is the length of the rectangle? "))
re_width = float(input("What is the width of the rectangle? "))
#The area is the lenght multiplied by the width.
rectangle_area = re_length * re_width
#printing results
print(f'The area of the square is: {rectangle_area}')

#Calculating the area of a circle
#Declaring variables and asking for a value
ci_radius = float(input("What is the radius of the circle? "))
#The area is Pi (you can use 3.14) multiplied by the radius squared
circle_area = 3.14 * (ci_radius**2)
#printing results
print(f'The area of the square is: {circle_area}')



#Stretch  Challenge
#1
#Calculating the area of a circle using math library
ci_radius = float(input("What is the radius of the circle in centimeters? "))
circle_area = math.pi * (ci_radius**2)
print(f'The area of the square in centimeters is: {circle_area:.1f}')

#2
#using the same variable for many purposes
var_stretch = float(input("Please insert a new value for the Stretch Challenge"))
#area of a square
sq_area = var_stretch**2
#area of a circle
circ_area = math.pi * (var_stretch**2)
#volume of a cube
vol_cube = var_stretch ** 3
#volume of a sphere with the same radius
vol_sphere = (4*math.pi*(circ_area**3))/3

#printing results
print(f'The area of the square is: {sq_area}')
print(f'The area of the square is: {circ_area}')
print(f'The volume of the cube is {vol_cube}')
print(f'The volume of the sphere is {vol_sphere}')

#3
#cm to meters
#Calculating the area of a square
sq_length = float(input("What is the length of a side of the square in centimeters? "))
square_area = sq_length**2
print(f'The area of the square in centimeters is: {square_area} cm²')
print(f'The area of the square in meters is: {square_area/10000} m²')

#Calculating the area of a rectangle
re_length = float(input("What is the length of the rectangle in centimeters? "))
re_width = float(input("What is the width of the rectangle in centimeters? "))
rectangle_area = re_length * re_width
print(f'The area of the square in centimeters is: {rectangle_area} cm²')
print(f'The area of the square in meter is: {rectangle_area/10000} m²')

#Calculating the area of a circle
ci_radius = float(input("What is the radius of the circle in centimeters? "))
circle_area = 3.14 * (ci_radius**2)
print(f'The area of the square in centimeters is: {circle_area} cm²')
print(f'The area of the square in meters is: {circle_area/10000} m²')
