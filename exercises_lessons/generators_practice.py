#!/usr/bin/python3

'''
Generators vs. Lists
[] vs ()
'''

# List:
l1 = [a for a in range(3)]
# Generator:
g1 = (a for a in range(3))
print(f"List: {l1}\nGenerator: {g1}")

# 1.- Return a generator
def generate_generator():
    return (a for a in range(10))
print(generate_generator())

print(a for a in range(1))  # This prints a generator obj 

# 2.- Return a list
def list_generator():
    return [a for a in range(10)]
print(list_generator())

print([a for a in range(2)])  # This prints a list

'''
Yield function

To
'''
def generate_generator():
    yield (a for a in range(10))
    # It's the same as yield []

print("With Yield: ")
print(generate_generator())

def generate_generator():
    return (a for a in range(10))
    # It's the same as yield 

print("With return: ")
print(generate_generator())

def yielder():
    for a in range(3):
        if a == 2:
            yield a # This returns a generator

print(yielder())
