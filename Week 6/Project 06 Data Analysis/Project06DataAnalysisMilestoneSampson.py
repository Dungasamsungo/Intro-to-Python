
#Project 06: Data Analysis
# By: SAMSPSON CHINEDU NGOBI
# milestone instructions 

# Download the dataset
# Load the dataset in your Python program
# Iterate through the data line by line
# Split each line into parts
# Find the lowest value for life expectancy and the highest value for life expectancy in the dataset, 
# and display both values. (Note that at this point, you just need the value for this, not the year and the country for that value.)

print()

country_name = []
codes = []
year = []
life = []

with open("life-expectancy.csv") as file:
    next(file)
    for first_line in file:
        clean_line = first_line.strip()
        buffer = clean_line.split(",")

        country_name.append(buffer[0])
        codes.append(buffer[1])
        year.append(buffer[2])
        life.append(float(buffer[3]))  # Convert life expectancy to float

lowest = min(life)
highest = max(life)

print("Lowest Life Expectancy:", lowest)
print("Highest Life Expectancy:", highest)

print()