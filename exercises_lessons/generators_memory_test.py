#!/usr/bin/python3

'''
Exercise: Comparing the usage of lists and generators
for memory usage
'''

import memory_profiler as mem_profile
import random

names = ['name1', 'name2', 'name3', 'name3', 'name4', 'name5']
attributes = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

Mem1 = mem_profile.memory_usage()

print(f"{Mem1} MB") # [38.640625] MB

# Case 1: Generating a dictionary of 1000000 entries
def my_list(num):
    result = []
    for i in range(num):
        my_dict = {
                    'id': i,
                    'name': random.choice(names),
                    'attribute': random.choice(attributes)
                }
        result.append(my_dict)
    return result

# Case 2: Generator of 1000000 entries (Exactly the same data)
def my_generator(num):
    for i in range(num):
        my_dict = {
                    'id': i,
                    'name': random.choice(names),
                    'attribute': random.choice(attributes)
                }
        yield my_dict

# Use my_list OR my_generator to profile the performance and see the difference
test1 = my_list(1000000)       # ~ [310.24609375] MB
# test1 = my_generator(1000000)      # [38.640625] MB

# For my_generator, the memory usage DOES NOT change, even when unpacking the generator object:
# (Commented because it takes a lot of time to execute)
# counter = 0
# for i in test1:
#     for k, v in i.items():
#        if v == 'name4':
#            counter += 1
# print(counter)

# Profiling the memory at the end of the program ("test1" dicts in buffer)
Mem2 = mem_profile.memory_usage()
print(f"{Mem2} MB")

# Credits: Corey Schafer, Mashrur.
