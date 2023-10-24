# Function to calculate the windchill
def calculate_windchill(temperature, windspeed):
    windchill = 35.74 + 0.6215 * temperature - 35.75 * windspeed ** 0.16 + 0.4275 * temperature * windspeed ** 0.16
    return windchill

# Function to convert Celsius to Fahrenheit
def convert_CtoF(temperature):
    fahrenheit_value = temperature * (9/5) + 32
    return fahrenheit_value

temperature = float(input("What is the temperature? "))  # Prompt user for a temperature value
temperature_unit = input("Enter the temperature unit (F = Fahrenheit or C = Celsius): ")  # Prompt user for a temperature unit

# Convert temperature to Fahrenheit if the unit is Celsius
if temperature_unit.upper() == "C":
    temperature = convert_CtoF(temperature)

# Loop through wind speeds from 5 to 60 in increments of 5
for windspeed in range(5, 61, 5):
    windchill = calculate_windchill(temperature, windspeed)
    print(f"At temperature {temperature:.1f}F and wind speed {windspeed}mph, the windchill is: {windchill:.2f}F")
