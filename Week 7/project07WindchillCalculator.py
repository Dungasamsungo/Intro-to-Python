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
def calculate_windchill(temperature, windspeed):
    windchill = 35.74 + 0.6215 * temperature - 35.75 * windspeed ** 0.16 + 0.4275 * temperature * windspeed ** 0.16
    return windchill

# this function converts the celsius temperature to fehrenheit
def convert_CtoF(temperature):
    fahrenheit_value = temperature  * (9/5) + 32
    return fahrenheit_value


print()
temperature = float(input("What is the temperature? ")) #prompt user for a temp value
temperature_unit = input("Enter the temperature unit (F = Fahrenheit or C = Celsius): ") # promt user for a temp unit
print()
if temperature_unit.upper() == "C":
        temperature = convert_CtoF(temperature)

# Loop through wind speeds from 5 to 60 in increments of 5
for windspeed in range (5, 61, 5): 
    windchill = calculate_windchill(temperature, windspeed)
    print(f"At temperature {temperature:.1f}F, and wind spead {windspeed}mph, the windchill is: {windchill:.2f}f ")
print()





