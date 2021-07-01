#!/usr/bin/python3

string = "abcdef"

for index, char in enumerate(string):
    print(str(index),char)  # Regresa tuples con (index, char)

l1 = ["coche","moto"]
l2 = ["bmw","ducati"]

my_tuple = list(zip(l1,l2)) # zip() regresa un objeto (Generador); hay que hacer typecast a list()
print(my_tuple) # (nested) Lista con tuples
my_tuple = tuple(zip(l1,l2)) # zip() regresa un objeto (Generador); hay que hacer typecast a list()
print(my_tuple) # (nested) Tuple con tuples

# Para asignar objetos de lista a diferentes variables:
coche, moto = l2
print(coche, moto)
