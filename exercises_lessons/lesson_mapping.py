#!/usr/bin/python3

# Se explica la funcion del metodo str (Default)
my_string = "hello world"

print(str.capitalize("a")) # <- Es un metodo
print(my_string.capitalize())

# MAP:
# map(funcion, iterable)
string2 = ""
string2 = " ".join(map(str.capitalize, my_string))
print(string2)

# MAP 2 Ejemplo con lambda:

l1 = [10,20]
print(map(lambda x: x/2, l1))
