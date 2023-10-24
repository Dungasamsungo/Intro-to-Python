import math

# Plan 
# Write functions that accets a single value and calculates 
    #1 Area of a square 
    #2 Area of a rectangle 
    #3 Area of a circle 

# Promt user for the side of the square, store it in a variable and pass it to the function to compute the area.
#  get the result back and display it 

def square_area(value):
    area_calc = square_length**2
    return area_calc

def rectangle_area(value):
    area_calc = lenght * width
    return area_calc

def circle_area(value):
    area_calc = math.pi * (radius**2)
    return area_calc

print("Enter a shape to calculate the area: QSUARE / RECTANGLE / CIRCLE. ENTER 'Q' to quit")

shapes = ["square", "rectangle", "circle" , "Q"]
for shape in shapes:
    shape_type = input("What kind of Shape do you have: ").upper()

    if shape_type.lower() == shapes[0]:
        square_length = float(input("Enter the Lenght of a side of the square: "))
        area_of_square = square_area(square_length**2)
        print(area_of_square)


    elif shape_type.lower() == shapes[1]:
        lenght = float(input("Enter the lenght of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area_of_rectangle = rectangle_area(lenght * width)
        print(area_of_rectangle)


    elif shape_type.lower() == shapes[2]:
        radius = float(input("Enter the radius of the circle: "))
        area_of_circle = circle_area( math.pi * (radius**2))
        print(area_of_circle)

    elif shape_type == shapes[3]:
        print("Thank you, Bye bye")
        break

    else:
        print("Enter: SQUARE , RECTANGLE, CIRLCLE or Q to quit")
        continue






