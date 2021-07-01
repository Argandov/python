# Question 1: Given the two lists below, add all the elements in the second list
# to the end of the first list, then print out the first list. Choose the
# appropriate method to add these elements so that you don't end up with a list
# within a list (as in the first list 'my_courses' should only have string data, 
# not lists of strings).
my_courses = ['comp sci','economics','physics','astronomy']
new_courses = ['climate studies','artificial intelligence']
## Write your code below, 2 lines ##
my_courses.extend(new_courses)

## End question 1

# Question 2: Given the string below, add it to the end of my_courses list which
# you printed at the end of question 1, then print out my_courses
new_course = 'tennis'
## Write your code below, 2 lines
my_courses.append(new_course)
print(my_courses)

# End question 2

# Question 3: Choose the approprite method to delete 'economics' from my_courses
# list and print the resulting my_courses list.
## Write your code below, 2 lines
my_courses.remove("economics")
print(my_courses)

# End question 3

# Question 4: Given the integer list below, print the length of the list (number
# of integers in the list).
my_int_list = [9,6,13,7,27,99,104,100,10,16,42,64]
## Write your code below, 1 line
len(my_int_list)
# End question 4

# Question 5: Grab the second half of my_int_list using slice notation and print
# it to the screen
## Write your code below, 1 line
my_int_list[int(len(my_int_list)/2):]

# End question 5
