#!/usr/bin/python3

# Sets are randomly displayed lists. There is no indexing, no calling. At print(set), the order gets scrambled. Always.

# Convert list -> set
my_list = ['coches','motos']
print(type(set(my_list))) # list typecasted into a set

my_set = {'javascript','python'}
my_set2 = {'javascript','ruby'}

#####

# Union of both sets:
print(my_set.union(my_set2))
# Print differing data between 1 and 2nd set:
print(my_set.difference(my_set2)) 
# Print a common data in both:
print(my_set.intersection(my_set2))





