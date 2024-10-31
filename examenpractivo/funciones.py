from os import system 
system("cls")
'''1. Cargar secuencialmente eventos que contengan un id, un tipo de
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

#punto 1
def cargar (eventos, indice , id) :
    continuar = "si"
    while continuar == "si": 
        tipo_evento = input("Introduce el tipo de evento\n cumpleaños\n casamiento\n fiesta de 15\n bodas de oro\n ")
        while tipo_evento != "cumpleaños" and tipo_evento != "casamiento" and tipo_evento != "fiesta de 15" and tipo_evento != "bodas de oro":
            tipo_evento = input("Error, reintroduce un tipo de evento valido: \n cumpleaños\n casamiento\n fiesta de 15\n bodas de oro\n")
        salon_evento = input("Introduce el salón del evento \n puerto madero\n palermo\n san telmo \n ")
        while salon_evento != "puerto madero" and salon_evento != "palermo" and salon_evento != "san telmo" : 
            salon_evento = input("Error,reintroduce un salon de evento existente \n puerto madero\n palermo\n san telmo \n ")

        if indice == len(eventos):
            eventos += [[0,0,0]]
        id += 1


        eventos[indice][0] = id
        eventos[indice][1] = tipo_evento
        eventos[indice][2] = salon_evento
        continuar = input("desea ingresar otro evento o salon? (si_no): ")
        while continuar != "si" and continuar != "no" :
            continuar = input("desea ingresar otro evento o salon? (si_no): ")
        indice += 1
        print(eventos)


    return eventos , indice , id 

#2. Calcular por cada salón la cantidad total de fiestas realizadas de cada tipo. Utilizar una función.

def calcular_consulta_recaudacion_calcular_mas_5M(eventos, menu):
    pu_con_bodas = 0
    pu_con_cum = 0
    pu_con_casa = 0
    pu_con_fies = 0
    pa_con_bodas = 0
    pa_con_cum = 0
    pa_con_casa = 0
    pa_con_fies = 0
    s_con_bodas = 0
    s_con_cum = 0
    s_con_casa = 0
    s_con_fies = 0
    con_general_pm= 0
    con_general_pa= 0
    con_general_s= 0
    acum_pm=0
    acum_pa=0
    acum_s=0
    for evento in eventos:        
        match evento [2]:
            case "puerto madero":
                    con_general_pm +=1 
                    match evento [1]:
                        case "cumpleaños":
                            pu_con_cum +=1
                            acum_pm += 2500000
                        case "casamiento":
                            pu_con_casa += 1
                            acum_pm += 2500000
                        case "fiesta de 15":
                            pu_con_fies += 1
                            acum_pm += 7500000
                        case "bodas de oro":
                            pu_con_bodas += 1
                            acum_pm += 5000000
            case "palermo":
                    con_general_pa += 1 
                    match evento [1]:
                        case "cumpleaños":
                            pa_con_cum +=1
                            acum_pa += 2500000
                        case "casamiento":
                            pa_con_casa += 1
                            acum_pa += 2500000
                        case "fiesta de 15":
                            pa_con_fies += 1
                            acum_pa += 7500000
                        case "bodas de oro":
                            pa_con_bodas += 1
                            acum_pa += 5000000
            case "san telmo":
                    con_general_s += 1
                    match evento [1]:
                        case "cumpleaños":
                            s_con_cum +=1
                            acum_s += 2500000
                        case "casamiento":
                            s_con_casa += 1
                            acum_s += 2500000
                        case "fiesta de 15":
                            s_con_fies += 1
                            acum_s += 7500000 
                        case "bodas de oro":
                            s_con_bodas += 1
                            acum_s += 5000000




    if menu == "2" :
        resultado=\
        f'''
        puerto madero:
        cumpleaños : {pu_con_cum}
        casamiento : {pu_con_casa}
        fiesta de 15 : {pu_con_fies}
        bodas de oro : {pu_con_bodas}

        palermo:
        cumpleaños : {pa_con_cum}
        casamiento : {pa_con_casa}
        fiesta de 15 : {pa_con_fies}
        bodas de oro : {pa_con_bodas}

        san telmo:
        cumpleaños : {s_con_cum}
        casamiento : {s_con_casa}
        fiesta de 15 : {s_con_fies}
        bodas de oro : {s_con_bodas}
        '''
    elif menu == "3":
        puerto_madero_maximo = encontrar_numero_mayor (pu_con_cum,pu_con_casa,pu_con_fies,pu_con_bodas)
        san_telmo_maximo = encontrar_numero_mayor (s_con_cum,s_con_casa,s_con_fies,s_con_bodas)
        palermo_maximo = encontrar_numero_mayor (pa_con_cum,pa_con_casa,pa_con_fies,pa_con_bodas)

        resultado=\
        f'''
        puerto madero: el evento mas realizado fue {puerto_madero_maximo}
        palermo: el evento mas realizado fue {palermo_maximo}
        san telmo: el evento mas realizado fue {san_telmo_maximo}
        '''
#4 Calcular la recaudación de cada salón, teniendo en cuenta que disponemos de un vector con los valores de cada tipo de evento. Generar una función

    elif menu =="4": 
        resultado=\
        f'''
        puerto madero : {acum_pm}
        palermo : {acum_pa}
        san telmo: {acum_s}
        '''
        #5 Calcular la cantidad de salones que hayan recaudado más de $5.000.000 en casamientos.
    elif menu == "5": 
        resultado = ""
        puerto_madero_recu_casamiento = pu_con_casa * 2500000 
        palermo_recu_casamiento = pa_con_casa * 2500000 
        san_telmo_recu_casamiento = s_con_casa * 2500000 

        if puerto_madero_recu_casamiento < 5000001:
            pass
        else:
            resultado += f"puerto madero recaudo mas de 5000000, especificamente {puerto_madero_recu_casamiento}\n" 
        if palermo_recu_casamiento < 5000001:
            pass
        else:
            resultado += f"palermo recaudo mas de 5000000, especificamente {palermo_recu_casamiento}\n" 
        if san_telmo_recu_casamiento < 5000001:
            pass
        else:
            resultado += f"san telmo recaudo mas de 5000000, especificamente {san_telmo_recu_casamiento}" 
    else: 
        s_respuesta = 0
        pa_respuesta = 0
        pm_respuesta = 0
        if pu_con_bodas != 0:
            pm_respuesta = (pu_con_bodas/con_general_pm)*100
        if pa_con_bodas != 0:
            pa_respuesta = (pa_con_bodas/con_general_pa)*100
        if  s_con_bodas != 0:  
            s_respuesta = (s_con_bodas/con_general_s)*100
        resultado = encontrar_el_pocentaje_mayor (pm_respuesta,pa_respuesta,s_respuesta)
    return resultado

#3. Consultar el nombre del evento más realizado en cada salón. Utilizar función.


def encontrar_numero_mayor(num_uno: int, num_dos: int, num_tres: int ,num_cuatro: int) ->int:
    '''
    Encuentra el numero mayor 
    '''
    if num_uno == num_dos and num_dos == num_tres and num_dos == num_cuatro:
        resultado = "son todos iguales "
    else:
        if num_uno == num_tres and num_uno == num_cuatro and num_uno > num_dos: 
            resultado = "cumpleaños, casamiento y fiesta de 15 tienen la misma cantidad de eventos"
        elif num_uno > num_dos and num_uno > num_tres and num_uno > num_cuatro: 
            resultado = "cumpleaños"
        elif num_dos >= num_tres and num_dos >= num_cuatro: 
            resultado = "casamiento"
        elif num_tres >= num_cuatro:
            resultado = "fiesta de 15"
        else:
            resultado = "boda de oro"

    return resultado


#6 Calcular el porcentaje de bodas de oro realizadas en cada salón. Mostrar el que haya realizado el mayor porcentaje.
def encontrar_el_pocentaje_mayor (num1 , num2, num3):
    
    if num1 == num2 and num2 == num3:
        resultado = f"tienen todos el mismo porcentaje, el cual es {num1}%"
    else:
        if num1 == num3 and num1 > num2: 
            resultado = f"puerto madero y san telmo tienen el mismo porcentaje , el cual es {num1}%"
        elif num1 == num2 and num1 > num3:
            resultado =  f"puerto madero y palermo tienen el mismo porcentaje , el cual es {num1}%"
        elif num1 > num2 and num1 > num3:
            resultado = f"puerto madero es el que tiene mayor porcentaje con {num1}% de bodas de oro"
        elif num2 >= num3:
            if num2 == num3:
                resultado= f"palermo y san telmo tienen el mismo porcentaje,  el cual es {num2}%" 
            else:
                resultado = f"palermo es el que tiene mayor porcentaje con {num2}% de bodas de oro"
        else:
            resultado = f"san telmo es el que tiene mayor porcentaje con {num3}% de bodas de oro"
    
    return resultado
