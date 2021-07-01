#!/usr/bin/python3

'''
Exercise: Comparing the usage of lists and generators
for memory usage
'''

import memory_profiler as mem_profile
import random

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

Mem1 = mem_profile.memory_usage()

print(f"{Mem1} MB") # [38.640625] MB

# Case 1: Generating a dictionary of 1000000 entries
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

# Case 2: Generator of 1000000 entries (Exactly the same data)
def people_gen(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# Use people_list OR people_gen to profile the performance and see the difference
# people = people_list(1000000)       # ~ [310.24609375] MB
people = people_gen(1000000)      # [38.640625] MB

# For people_gen, the memory usage DOES NOT change, even when unpacking the generator object:
# (Commented because it takes a lot of time to execute)
# counter = 0
# for i in people:
#     for k, v in i.items():
#        if v == 'Thomas':
#            counter += 1
# print(counter)

# Profiling the memory at the end of the program ("people" dicts in buffer)
Mem2 = mem_profile.memory_usage()
print(f"{Mem2} MB")

# Credits: Corey Schafer, Mashrur.
