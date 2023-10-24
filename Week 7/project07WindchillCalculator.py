# PROJECT O7 WINDCHILL
# BY SAMPSON NGOBI

# Plan

# write a function that calculates the windchill 
# write a function that converst from C to F 

# prompt user for a temperature value
# Prompt for the temperature unit
# check if the unit is C and convert it to F using the function 

# Loop through 5 to 60 counting in fives and calculate the windchill for each wind speed using the function 

# display the windchill values to 2 decimal places 


# this function calculates the windchill value
def calculate_windchill(value):
    windchill = (35.74 + 0.6215) * T - 35.75 * V ** 0.16 + 0.4275 * T * V ** 0.16
    return windchill

# this function converts the celsius temperature to fehrenheit
def convert_CtoF(value):
    fahrenheit_value = T  * (9/5) + 32
    return fahrenheit_value



