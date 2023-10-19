
# This doesn't close the file 
course_file = open("courses.txt")
 
for line in course_file:
    print(line)


# this opens and closes the file 
with open("courses.txt") as course_file:
    for line in course_file:
        parts = line.split(",")
        course_name = parts[0]
        grade = parts[1]
        print


