from collections import OrderedDict
# Question 1: Create an empty dictionary called life_book of type OrderedDict. 
# From Python 3.6 onwards dictionaries maintain the order in which they were 
# created, however, this coding environment uses an earlier version of Python 3.
# Therefore, use OrderedDict in this case, example my_dict = OrderedDict().
# Once created, use the print function to print it.
## Write your code below, 2 lines
life_book = {3:3333, '22':2222,1:1111, '2':'2222'}
my_dict = OrderedDict(life_book)
print(my_dict)


# End question 1

# Question 2: Add the following key, value pair to the life_book dictionary
# 'pet' -> 'dog', so the key is pet and the value is dog and then print it.
## Write your code below, 2 lines
life_book = {'pet':'dog'}

# End question 2

# Question 3: Add the following key, value pairs to the dictionary
# 'second_pet' -> 'cat'
# 'first_child' -> 'boy'
# 'second_child' -> 'girl'
# Once added, print the dictionary.
## Write your code below, variable lines


# End question 3

# Question 4: Update the value associated with key 'pet' to be 'hamster', then
# print the dictionary.
## Write your code below, 2 lines


# End question 4

# Question 5: Given the dictionary below, use the items() method and save
# the value of all the key value pairs to the variable courses_iterable.
my_courses = {'a':'python', 'b':'javascript', 'c':'ruby on rails', 'd':'machine learning', 'e':'ai'}
## Write your code below, 1 line
courses_iterable = my_courses.items()
# End question 5
