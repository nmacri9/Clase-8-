import math
#A 
lista_ingresos = [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
                    9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
#A
porcentaje_20 = 4
suma_mas_gana = 0
mayores = [0] * 4

for i in range (porcentaje_20):
    # Calcular el promedio de ingresos/hora del 20% que más gana
    mayor = -1
    for numero in lista_ingresos:
        if numero > mayor and numero not in mayores:
            mayor = numero
    mayores[i] = mayor
    suma_mas_gana += mayor

#B Calcular el promedio de ingresos/hora de todos los respondentes.
def promediar_ingresos_hora (lista_ingresos: float) -> float:
    contador = 0
    suma_ingresos = 0
    
    for numero in lista_ingresos:
        if numero != 0:
            suma_ingresos += numero
            contador += 1
        else: 
            return 1
    resultado = suma_ingresos / contador
    return resultado

#c
def calcular_repetido(lista):
    lista_repetidos = []
    contador_repetidos = 0

    for numero in lista:
        if numero not in lista_repetidos:
            repeticiones = 0
            for n in lista:
                if n == numero:
                    repeticiones += 1
            lista_repetidos += [numero]  # Usar concatenación para agregar el número
            if repeticiones > contador_repetidos:
                contador_repetidos = repeticiones

    resultado = []
    for numero in lista_repetidos:
        if lista.count(numero) == contador_repetidos:
            resultado += [numero]  # Usar concatenación para crear el resultado

    return resultado

#d
# d) Media geométrica
producto = 1
for ingreso in lista_ingresos:
    producto *= ingreso
media_geometrica = producto ** (1 / len(lista_ingresos))
print(f"Media geométrica: {media_geometrica}")

#e
for i in range(len(lista_ingresos) - 1, -1, -1):
    print(f"El indice es {i}")
    print(f"El valor es {lista_ingresos[i]}")



#2
lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ["Juan", "Matias", 'Carla', 'Susana', 'Olivia', 'Carlos', 'Daniel', 'Jimena','Mariela', 'Ignacio']

edad_min = lista_edad[0]
edad_max = lista_edad[0]
nombre_mas_joven = lista_nombres[0]
nombre_mas_grande = lista_nombres[0]

# Iteramos sobre las listas para encontrar los valores
for i in range(len(lista_edad)):
    if lista_edad[i] < edad_min:
        edad_min = lista_edad[i]
        nombre_mas_joven = lista_nombres[i]
    elif lista_edad[i] > edad_max:
        edad_max = lista_edad[i]
        nombre_mas_grande = lista_nombres[i]

print(f"El más joven es {nombre_mas_joven} con {edad_min} años.")
print(f"El más grande es {nombre_mas_grande} con {edad_max} años.")

#B 
for edad in lista_ingresos:
    if edad > 65:
        print('Se ha encontrado una persona +65.')
        break

#C
suma_edades = 0
contador_edades = 0
for edad in lista_edad:
    if edad > 40:
        suma_edades += edad
        contador_edades += 1
    else: 
        continue
media_etaria = suma_edades / contador_edades
print(f'La media etaria es {media_etaria:.2f}')

#3
lista_nueva_nombre = [0] * 1
lista_nueva_sexo = [0 ] * 1
lista_nueva_horas = [0 ] * 1
lista_nueva_ingresos  = [0 ] * 1

#  cargar listas secuencialmente
for i in range(len(lista_nueva_nombre)):
    lista_nueva_nombre[i] = input(f"Ingrese un nombre para la posición {i}: ")
print(lista_nueva_nombre)
for i in range(len(lista_nueva_sexo)):
    lista_nueva_sexo[i] = input(f"Ingrese un sexo para la posición {i}: ")
print(lista_nueva_sexo)
for i in range(len(lista_nueva_horas)):
    lista_nueva_horas[i] = input(f"Ingrese un horas para la posición {i}: ")
print(lista_nueva_horas)
for i in range(len(lista_nueva_ingresos)):
    lista_nueva_ingresos[i] = input(f"Ingrese un ingresos para la posición {i}: ")
print(lista_nueva_ingresos)

lista_respondentes = (lista_nueva_nombre + lista_nueva_sexo + lista_nueva_horas + lista_nueva_ingresos)
print (lista_respondentes)

#5




#6
def pedir_numeros (numero: int , rango_min= 0, rango_max = 1000) -> list:


    lista_numeros = []
    while len(lista_numeros) < 10:
        numero = int(input('Ingrese un numero:'))
        if rango_min <= numero <= rango_max:
            lista_numeros.append (numero)
        else:
            print('El numero esta fuera de los rangos (0-1000)')
    return lista_numeros


#7
nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]
def encontrar_menores(nombres, edades):
    # Encontrar la menor edad
    menor_edad = min(edades)
    # Filtrar los nombres de las personas con la menor edad
    menores = [(nombres[i], edades[i]) for i in range(len(edades)) if edades[i] == menor_edad]
    
    return menores
menores = encontrar_menores(nombres, edades)
print  (F'El nombre y edad de los menores es {menores}:')


#8 
lista_nueva = [10, 15, 42 , 'Nico', False, True]
def verificar_tipos(lista_nueva):

    tipos = {type(elemento) for elemento in lista_nueva}  # Crear un conjunto con los tipos
    tipos_permitidos = {int, str, bool, float}
    
    if len(tipos) == 1:
        return f"Todos los elementos son del mismo tipo: {tipos}"
    else:
        # Retornar información de tipos
        return f"Los tipos de elementos en la lista son: {tipos}"
# Llamar a la función
resultado = verificar_tipos(lista_nueva)
print(resultado)

#9
lista_cualquiera = [0] * 5


# cargar elementos de manera aleatoria

def validar_tipo(valor):
    tipos_permitidos = {int, str, bool, float}
    """Función para validar el tipo de dato ingresado y convertirlo."""
    match valor:
        case _ if valor == int:  # Verificar si es un número entero
            return int(valor)
        case "true":  # Verificar booleano True
            return True
        case "false":  # Verificar booleano False
            return False    
    while cargar == "s":
        i = int(input("Ingrese posición de la lista: "))
        valor = input("Ingrese valor para la lista: ")

    tipo_valor = type(validar_tipo(valor))  # Validar el tipo de dato
    
    if tipo_valor in tipos_permitidos:
        lista_cualquiera[i] = validar_tipo(valor)  # Almacenar el valor validado
        print(f"Valor agregado en la posición {i}: {lista_cualquiera[i]}")
    else:
        print(f"Tipo no permitido. No se puede agregar.")

    cargar = input("¿Quiere cargar otro elemento? s/n :")

print('Lista final:')
for elemento in lista_cualquiera:
    print(elemento)