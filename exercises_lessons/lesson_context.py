#!/usr/bin/python3

"""
Teniendo una lista num[], si hacemos referencia a ella con una variable num[0], sólo se queda como referencia.
Si pasamos la lista a procesar como num, se procesa como lista y no como referencia (Modificación global)

"""

# 2 Funciones idénticas:
def function(num):
    num += 1                # Este índice no es global
    return num

def function2(num):
    num[0] += 1             # Este índice SÍ es global
    return num

# Estas 3 calls hacen exactamente lo mismo:
num = [0]
print(f"Initial num\t -> {num}")
print("\n" + "*"*10+"Modificación en contexto de la función"+"*"*10 + "\n")
function(num[0])            # Este índice no se modifica globalmente
print(f"Function(num)\t -> {num}")
# Es lo mismo que:
num = [0]
function2(num.copy())       # Este índice NO se modifica globalmente
print(f"Function(num)\t -> {num}")
num = [0]
function2(num[:])            # Otra forma de hacerlo (Ojo: function2 porque function no hace num iterable)
print(f"Function(num)\t -> {num}")

# Esta vez, se modifica globalmente
print("\n" + "*"*10+"Modificación Global"+"*"*10 + "\n")
num = [0]
function2(num)              # Este índice SI se modifica globalmente
print(f"num\t\t -> {num}")

