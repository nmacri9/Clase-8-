from algoritmos.modulo1 import *

lista = [1, 3, 5, 6, 99, 10, 88, 4]

indice = buscar_lineal(lista , 10)
"""  buscar lineal / buscar_binaria"""

if indice is None:
    print('No esta el numero en la lista.')
else:
    print(f'El indice de la lista donde eesta el numero es {indice}')

