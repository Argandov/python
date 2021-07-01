# First we created a function to convert a string read in from data.txt
# to objects with which we can create student objects, we called
# this function prep_record below

file_name = "data.txt"

def prep_record(line):
    line = line.split(":")
    first_name, last_name = line[0].split(",")
    course_details = line[1].rstrip().split(",")
    return first_name, last_name, course_details

with open(file_name) as f:
    for line in f:
        print(line.strip())
        first_name, last_name, course_details = prep_record(line)
        print(first_name, last_name, course_details)

# We then created the prep_to_write function which takes in the
# attributes of student objects and creates a string in the format
# of other records in the data.txt file

def prep_to_write(first_name, last_name, courses):
    full_name = first_name+','+last_name
    courses = ",".join(courses)
    return full_name+':'+courses

to_write = prep_to_write(first_name, last_name, course_details)
print(to_write)
