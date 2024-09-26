"""la_lista = [1] * 5
#Cantidad numeros que hay. (len)
print(la_lista)

for i in range(len(la_lista)) :
    la_lista[i] == input(f'ingrese nombre para posicion {i}: ')
# i = indice, posicion en el listado
print (la_lista)"""

lista = [0] * 5

for elemento in lista:
    print (elemento)

carga = 's'

i = (int(input('Ingrese posicion de lista: ')))
valor = input('Ingresar valor de la lista: ')
carga = input('Ingresar otro elemento? s/n')