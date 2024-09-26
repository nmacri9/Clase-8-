"""
 Supongamos que está trabajando en desarrollar el programa de carga de una encuesta.
 1- Pedir al usuario que ingrese nombre y apellido del encuestado, guardarlo como string.
 2- Pedir al usuario que ingrese el salario mensual del encuestado y guardarla como entero.
 3- Pedir al usuario que ingrese la cantidad de horas trabajadas en la semana anterior por el
 encuestado y guardarlo como entero. Validar que sea un valor entre 0 y 120
 4- Calcular el ingreso horario del encuestado (ingreso dividido por horas trabajadas) y
 generar una respuesta por pantalla con todos los datos ingresados para verificar que estén
 bien cargados.
 5- Dada la siguiente lista de ingresos horarios:
 [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
 9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
 a) Calcular el promedio de ingresos/hora del 20% que más gana.
 b) Calcular el promedio de ingresos/hora de todos los respondentes.
 c) Buscar cuál es el valor que más se repite.
 d) Calcular la media geométrica
"""
suma_ingresos = 0

nombre = str(input ('Ingrese el nombre y apellido del encuestado: '))

salario = int(input('Ingrese el salario mensual: '))

horas_trabajadas = int(input('Ingrese sus horas trabajadas la semana anterior (entre 0 y 120): '))

while horas_trabajadas < 0 or horas_trabajadas > 120:
    horas_trabajadas = int(input("Error: El valor debe estar entre 0 y 120. Intentar de nuevo: "))

ingreso_horario = salario / horas_trabajadas

print (F'Su nombre y apellido es {nombre}, su salario es {salario}, sus horas: {horas_trabajadas} y su ingreso horario es de {ingreso_horario}.')


lista_ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9 , 32, 15, 6, 50, 19, 26, 65, 10, 18 ]

#a Calcular el promedio de ingresos/hora del 20% que más gana
ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18]

porcentaje_20 = ((len(ingresos) * 0.20))

maximo_1 = ingresos[0]
for numero in ingresos:
    if numero > maximo_1:
        maximo_1 = numero
maximo_2 = ingresos[0]
for numero in ingresos:
    if numero == maximo_2 and maximo_1 > numero:
        maximo_2 = numero
maximo_3 = ingresos[0]
for numero in ingresos:
    if numero == maximo_3 and maximo_2 > numero:
        maximo_3 = numero
maximo_4 = ingresos[0]
for numero in ingresos:
    if numero == maximo_4 and maximo_3 > numero:
        maximo_4 = numero

promedio = float((maximo_1 + maximo_2 + maximo_3 + maximo_4) / porcentaje_20 )

print(f'El promedio es de {promedio}')

#B Calcular el promedio de ingresos/hora de todos los respondentes.
suma_ingresos = 0
for ingreso in lista_ingresos:
    suma_ingresos += ingreso
#b Calculamos el promedio
promedio_ingresos = suma_ingresos / len(lista_ingresos)

# Mostramos el resultado
print(f"El promedio de ingresos por hora de todos los respondentes es:", {promedio_ingresos})

#C El valor que mas se repite

conteo = 0
num_mas_repetido = 0

for numero in lista_ingresos:
    conteo = numero
    for num in lista_ingresos:
        if conteo == num:
            num_mas_repetido += 1




print(f'el numero mas repetido es {num_mas_repetido}')
#D calcular medida geometrica.

producto = 1

for numero in lista_ingresos:
    producto *= numero

media_geometrica = producto ** (1 / len(lista_ingresos))

print (f'La media geometrica es {media_geometrica}')

#6 El mas joven y mas grande
maximo_edad = 0
minimo = 0
bandera = True
bandera_minimo = True

lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ['Juan', 'Matias', 'Carla', 'Susana', 
                'Olivia', 'Carlos', 'Daniel', 'Jimena', 'Mariela', 'Ignacio']

for index in range(len(lista_edad)):
    if bandera == True:
        nombre_max = lista_nombres [index]
        edad_maximo = lista_edad [index]
        nom_minimo = lista_nombres [index]
        edad_minimo= lista_edad [index]
        bandera = False
    else: 
        if lista_edad [index] > edad_maximo:
            nombre_max = lista_nombres [index]
            edad_maximo = lista_edad [index]

        elif lista_edad [index] < edad_minimo:
            nom_minimo = lista_nombres [index]
            edad_minimo = lista_edad [index]


print (f'La edad minima es {edad_minimo} y es de {nom_minimo}')
print(f'La edad mas alta es {edad_maximo} y es de {nombre_max}')



#6
contador = 0
acumulador_Edades = 0

for edad in lista_edad:
    if lista_edad > 40:
        contador += 1
        acumulador_Edades += lista_edad

print (acumulador_Edades / contador)

#7 
lista_numeros = [14,99,8,15,17,33,19,24,12,10]

multiplos_Cinco = 0

for numero in lista_numeros:
    if numero % 5 == 0:
        multiplos_Cinco += 1

print (f'Los multiplos de 5 son {multiplos_Cinco}')


