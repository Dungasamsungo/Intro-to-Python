
# I showed creativity by adding a code that checks the year provided by users
# and informs them when there is no data found for the year they provided 

#Project 06: Data Analysis
# By: SAMSPSON CHINEDU NGOBI
# Stretch challenge instructions 
# Allow the user to type in a year, then, find the average life expectancy for that year. 
# Then find the country with the minimum and the one with the maximum life expectancies for that year.



print()

country_name = []
codes = []
year = []
life = []

with open("life-expectancy.csv") as file:
    next(file)
    for first_line in file:
        buffer = first_line.split(",")

        country_name.append(buffer[0])
        codes.append(buffer[1])
        year.append(int(buffer[2]))
        life.append(float(buffer[3]))  # Convert life expectancy to float

lowest = min(life)
highest = max(life)
min_index = life.index(lowest)
max_index = life.index(highest)



   
print()
print(f"The overall max life expectancy is: {highest} from {country_name[max_index]} in {year[max_index]}")
print(f"The overall min life expectancy is: {lowest} from {country_name[min_index]} in {year[min_index]}")
print()

target_year = int(input("Enter the year of interest: "))


target_year_data = [life[i] for i in range(len(year)) if year[i] == target_year]

if not target_year_data:
    print(f"No data found for the year {target_year}.")
else:
    average_life = sum(target_year_data) / len(target_year_data)
    min_life_expectance = min(target_year_data)
    max_life_expectance = max(target_year_data)
    min_life_index = target_year_data.index(min_life_expectance)
    max_life_index = target_year_data.index(max_life_expectance)

    print(f"For the year {target_year}:")
    print(f"The average life expectancy across all countries was: {average_life:.2f}")
    print(f"The max life expectancy was {max_life_expectance} in {country_name[max_life_index]}")
    print(f"The min life expectancy was {min_life_expectance} in {country_name[min_life_index]}")





print()

