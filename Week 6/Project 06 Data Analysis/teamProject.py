# # Team Project 

# Core Requirements
# Have your program open the HR System file, read through it line by line, and at this point, simply display the line to the screen.
# Split the line into parts and change your display, so that it shows only the names (instead of the whole line).
# For each line, get the name and the job title for each person, and display those to the screen.

with open("hr_system.txt") as staff_list:
    
    for line in staff_list:
        staff = line.split(" ")
        name = staff[0]
        job_title = staff[2]
        print(f"Name: {name} Title: {job_title}") 


# Stretch Challenge

# Strip off any leading and trailing whitespace from each line.In addition to the name and the job title, 
# also access the salary and the ID number and save them into variables. Display all four values in this 
# format: name (ID: id_number), job_title - $salary. 
# Don't forget to convert the salary to a number and display it with two decimals.
# The following shows the first few lines of expected output at this point.

# Instead of displaying the salary information, calculate and display a paycheck amount for the employee. 
# Assume that they are paid twice a month.

#Change the program so that it generates bonuses for anyone who is an engineer. 
# For each of these employees, add $1000 to their paycheck amount.

# Stretch Challenge 1
print()
with open("hr_system.txt") as staff_list:
    
    for line in staff_list:
        staff = line.split(" ")

        name = staff[0]
        staff_id = staff[1]
        job_title = staff[2]
        salary = float(staff[3])
        print(f"Name: {name} (ID: {staff_id}) Title: {job_title} - ${salary:.2f}") 

print()

# Stretch Challenge 2

with open("hr_system.txt") as staff_list:
    
    for line in staff_list:
        staff = line.split(",")

        name = staff[0]
        staff_id = staff[1]
        job_title = staff[2]
        salary = float(staff[3])
        paycheck = salary / 24
        
        if job_title.lower() == "engineer":
            paycheck += 1000

        print(f"Name: {name} (ID: {staff_id}) Title: {job_title} - ${paycheck:.2f}") 

print()