#!/usr/bin/python3

# Compara 2 listas, selecciona el menor numero en cada iteracion, y forma una tercera lista con estos numeros.
# Ej. [0,6] y [5,2] regresa [0,2]

def func_0(sorted_l1,sorted_l2):
    if len(sorted_l1) != len(sorted_l2):
        return 0
    l3 = [] # <- List comprehension?

    for i in range(len(l1)):
        if sorted_l1[i] >= sorted_l2[i]:
            l3.append(sorted_l2[i])
        else:
            l3.append(sorted_l1[i])
    return l3

def func_1(munch_it,l1,l2):
    # func_0 = munch_it; se puede usar otro nombre como argumento
    return munch_it(sorted(l1),sorted(l2))

l1 = [1,13,2,4,2]
l2 = [5,23,4,2,1]

print(func_1(func_0,l1,l2))


def func_3(string):
    # Regresa el string con "|" entre cada caracter del input
    output = ""
    for char in string:
        output += "|" + char # <- Esto regresa un string

    #output = ["|" + char for char in string] # <- Esto regresa una lista
    return output

