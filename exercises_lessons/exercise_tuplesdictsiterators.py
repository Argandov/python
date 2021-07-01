import random

# Question 1: Use list comprehension to update the code below and
# assign my_list to be a list of 200 random integers ranging in values
# between 25 and 500. Hint: Use the randint function
my_list = [random.randint(25,501) for num in range(0,200)]
print(f"Q1: {my_list}")

# Question 2 (4 parts): Cast my_list to a set and re-assign to my_list as a list.
# How many duplicate values were removed?
initial_size = len(my_list) # replace the code to the left

my_list = list(set(my_list))
print(f"{str(initial_size-len(my_list))} items were removed from the list")
# print(f"Initial size of my_list: {initial_size}")
# cast the list to a set to remove duplicates and re-assign to my_list as a list
#my_list = my_list # replace the code to the left
final_size = len(my_list) # replace the code to the left
print(f"Final size of my_list after removing duplicates: {final_size}")

dups_removed = initial_size-len(my_list)  # replace the code to the left
print(f"Number of integers removed: {dups_removed}")
print('-'*40)
print()
# Question 3: What is the largest integer in my_list?
largest_val = max(my_list) # replace the code to the left
print(f"Largest integer in my_list: {largest_val}")
print('-'*40)
print()
# Question 4: What is the smallest value in my_list?
smallest_val = min(my_list) # replace the code to the left
print(f"Smallest integer in my_list: {smallest_val}")
print('-'*40)
print()
# Question 5: Create a tuple with the exact same values as my_list
# name it my_tuple
my_tuple = tuple(my_list) # replace the code to the left
print(my_tuple)
# Question 6: What are the last 3 values of my_tuple?
my_tuple_last_val = my_tuple[-1] # replace the code to the left
my_tuple_sec_last_val = my_tuple[-2]  # replace the code to the left
my_tuple_third_last_val = my_tuple[-3] # replace the code to the left
print(f"The last 3 values of the tuple are {(my_tuple_third_last_val,my_tuple_sec_last_val,my_tuple_last_val)}")
print('-'*40)
print()
# Question 7: Create a new tuple with all the values of my_tuple in
# reversed order
my_new_tuple = my_tuple[::-1]# replace the code to the left
print(my_new_tuple)

# Question 8: Does the first value of my_new_tuple match my_tuple_last_val?
# Enter in the conditional below that will evaluate to True or False
comparison = my_tuple_last_val == my_new_tuple[0] # replace the code to the left
print(f"First integer of my_tuple matches last integer of my_new_tuple is a {comparison} statement")
print('-'*40)
print()

# Question 9: Create a new tuple with the first 5 values of my_new_tuple
my_other_tuple = my_new_tuple[0:5] # replace the code to the left
print(f"My newly created 5 integer tuple is {my_other_tuple}")
print('-'*40)
print()

# Question 10: Do the integers (ignore order) of my_other_tuple match the values of
# the last 5 integers in my_list? replace the boolean below with
# a conditional that evaluates to True or False. You can use other variables
# below as you need to complete this.
for a in range(0,5):
    if not my_other_tuple[int(a)] in my_list[-5:]:
        tuple_and_list_comp = False
        break
    else:
        tuple_and_list_comp = True
print(f"Integers in my_other_tuple match the last 5 integers of my_list is a {tuple_and_list_comp} statement")
print('-'*40)
print()
# Question 11: Find the intersection between the following two sets and
# store it in my_match
my_requirements = {'ruby','python'}
available_languages = {"comp sci", "physics", "elec engr", "philosophy", "python"}
my_match = my_requirements.intersection(available_languages) # replace the code to the left
print(f"I can take {my_match} since I need it and it's available")
print('-'*40)
print()

# Question 12: Given the dictionary below, create a list called my_al_list
# which includes only the values (meaning) associated with each word.
# my_al_list should look like ['the round fruit of a tree of the rose family',
# 'an insect which cleans up the floor'......].
# Obviously do this programmatically and don't hardcode it, you may use
# other lines of code and variables as you see fit. Solution code has a couple of
# options displayed.

word_dict = {'a':
                {
                 'apple': 'the round fruit of a tree of the rose family',
                 'ant': 'an insect which cleans up the floor'
                },
             'b':
                {
                 'bad': 'of poor quaity or low standard',
                 'business': 'season 8 of GOT'
                }
            }

my_al_list = []
for section in word_dict.items():
    for k,v in section[1].items():
        my_al_list.append(v)
print(f"The meanings in the dictionary are {my_al_list}")
