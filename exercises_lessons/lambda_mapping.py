#!/usr/bin/python3

'''
2 Use cases:

- One-time functions
- mapping through a list, with a function.

'''

# One liner. Not for reuse, and single expressions:
my_lambda = lambda x: x+2
print(my_lambda)            # A function -object-
print(my_lambda(3))         # A function -call-


# To be passed into functions, useful for one-time use cases:
def my_math_func(x, y, f):
    return f(x, y)

lambda_func = lambda x, y: x*3 + y
print(my_math_func(1, 1, lambda_func))

# Is the same as:
def my_math_func(x, y, f):
    return f(x, y)

def multiplier(x, y):
    return x*3 + y

print(my_math_func(1, 1, multiplier))

# Note: Python Linters do not like Lambda, 
# "Do not assign a lambda expression. Use def"

# Mapping a lambda function:
l1 = [0, 1, 2, 4]
mul = lambda x: x+100

# Instead of:
'''
for value in l1:
    print(mul(value))
'''
# Mapping the Iterable:
result = map(mul, l1)
print(result)

# Mapping with string functions:
l2 = ['a', 'b', 'c', 'd']
result = map(str.capitalize, l2)

# in map(arg1, arg2) I cannot pass something complex to arg1, unless I pass in a previously defined function, like:
def my_string_function(string):
    return string + "-"
   
result = map(my_string_function, l2)
print(result)

# We can pass in a lambda function as an argument:
result = map(lambda x: x+x.capitalize()+" . ", l2)
print(result)

# New function, list comprehensions, mapping a list through a lambda expression:
from random import randint

my_list = [randint(1,10) for num in range(1,10)] # < 10 random numbers from 1-10
print(my_list)
my_new_numbers = map(lambda x: x*2, my_list)
print(my_new_numbers)
