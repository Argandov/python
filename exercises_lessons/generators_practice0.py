#!/usr/bin/python3

'''
generators, iterators
Yield, next, 

Funcs: next, iter, zip, yield

!! In Python3, zip, map, etc. return function objects
!! In Python2, they return values.

Python2 - zip(a,b) == Python3 - list(zip(a,b))

* This file contains a lot of redundant and repetitive generators
'''
# 
l1 = [0, 1, 3]
l2 = [0, 2, 4]

# This is a list:
l3 = [l1[a] for a in range(len(l1))]
# While this is a generator object:
print(l1[a] for a in range(len(l1)))

for a in range(len(l1)):
    print(l1[a])

for a in range(len(l1)):
    print(l1[a])

print("***********************************************")
# Case: A generator can only be used once
# In the second run, the generator is now empty

l3 = zip(l1, l2)

print(list(l3))
print(list(l3))

l3 = zip(l1, l2)
var = len(list(l3))     # 3: This is the last time l3 object can be used
print(list(l3))         # 0: Already used

# next() function for generator:

l3 = zip(l1, l2)

for a in range(len(l1)):
    print(next(l3))
# It's the same as:
'''
next(l3)
next(l3)
'''
print("---------------------------------")
l3 = zip(l1, l2)
next(l3)            # 1 iteration
print(next(l3))     # 2 iteration
next(l3)            # 3 iteration

#

l3 = zip(l1, l2)
iterator = iter(l3)
print(iterator)
print(next(iterator))   # 1
print(next(iterator))   # 2

# YIELD:


