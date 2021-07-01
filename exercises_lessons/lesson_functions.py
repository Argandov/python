# Funcionamiento de variables dentro de funciones, globalmente

def function(string, array=[]):
    array.append(string)
    print(array)

function("peras") # Regresa ['peras']
function("manzanas") # Regresa ['peras', 'manzanas']
# peras se queda almacenado en "array"
