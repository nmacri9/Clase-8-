from os import system 
system("cls")

from funciones import * 

'''Una empresa se dedica a la realización de eventos. Para ello cuentan con 3
salones en CABA, que se encuentran en Puerto Madero, Palermo y San
Telmo.
Los salones pueden realizar 4 tipos diferentes de eventos: cumpleaños,
casamientos, fiestas de 15 y bodas de oro.
La oficina central, recibe mensualmente una planilla de donde se indican la
cantidad de eventos realizados en cada salón.
Realizar un menú de opciones que permita:
1. Cargar secuencialmente eventos que contengan un id, un tipo de
evento y un salón correspondiente en el main.py
2. Calcular por cada salón la cantidad total de fiestas realizadas de cada
tipo. Utilizar una función.
3. Consultar el nombre del evento más realizado en cada salón. Utilizar
función.
4. Calcular la recaudación de cada salón, teniendo en cuenta que
disponemos de un vector con los valores de cada tipo de evento.
Generar una función.
5. Calcular la cantidad de salones que hayan recaudado más de
$5.000.000 en casamientos.
6. Calcular el porcentaje de bodas de oro realizadas en cada salón.
Mostrar el que haya realizado el mayor porcentaje.'''
menu1=\
'''1. Cargar eventos
2. Calcular por cada salón
3. Consultar el nombre del evento más realizado en cada salón.
4. Calcular la recaudación de cada salón.
5. Calcular la cantidad de salones que hayan recaudado más de $5.000.000 en casamientos.
6. Calcular el porcentaje de bodas de oro realizadas en cada salón.
7. salir 
eliga la opcion: '''
id = 0
indice = 0
eventos=[]
menu = 0
res = True
carga = [[1, "casamiento", "puerto madero"],[2, "bodas de oro", "puerto madero"],
         [3, "bodas de oro", "palermo"],[4, "casamiento", "puerto madero"],[5, "casamiento", "palermo"],
         [5, "casamiento", "palermo"],[6, "casamiento", "palermo"],[1, "casamiento", "puerto madero"] ]


while res :
    menu = input(f"{menu1}")
    match menu:
        case "1":
            carga , indice , id = cargar(eventos, indice , id)
            print(carga)
        case "2":
            if carga == []:
                print("intente cargar los datos primero")
            else:
                print(calcular_consulta_recaudacion_calcular_mas_5M(carga, menu))
        case "3":
            if carga == []:
                print("intente cargar los datos primero")
            else:
                print(calcular_consulta_recaudacion_calcular_mas_5M(carga, menu))
        case "4":
            if carga == []:
                print("intente cargar los datos primero")
            else:
                print(calcular_consulta_recaudacion_calcular_mas_5M(carga, menu))
        case "5":
            if carga == []:
                print("intente cargar los datos primero")
            else:
                print(calcular_consulta_recaudacion_calcular_mas_5M(carga, menu))
        case "6":
            if carga == []:
                print("intente cargar los datos primero")
            else:
                print(calcular_consulta_recaudacion_calcular_mas_5M(carga, menu))
        case "7":
            res= False
        case _ :
            print("la opcion ingresada es invalida")
        