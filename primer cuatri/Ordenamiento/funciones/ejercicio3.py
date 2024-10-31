Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria",
            "Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa",
            "Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def ordenar_nombre_puntos(Apellidos: list, Nombres: list, Nota = list)-> list:
    if type(Apellidos) != list or type(Nombres) != list or type(Nota) != list: 
        print('No son una lista.')
        return None
    n = len(Apellidos)
    for i in range(n):
        for j in range(0, n-i-1):
            #comparo apellidos
            if Apellidos [j] > Apellidos[j+1]:
                #intercambio apellidos
                Apellidos[j], Apellidos [j+1] = Apellidos [j+1], Apellidos[j]
                #intercambio nombres
                Nombres[j], Nombres[j+1] = Nombres[j+1], Nombres[j]
                #intercambio nota
                Nota[j], Nota[j+1] = Nota[j+1], Nota[j]
            #si apellidos son iguales
            elif Apellidos [j] == Apellidos [j+1]:
                #comparo nombres e intercambio
                if Nombres [j] > Nombres [j+1]:
                    Nombres [j], Nombres[j+1] = Nombres[j+1] , Nombres[j]
                    Nota[j], Nota[j+1] = Nota[j+1], Nota[j]
                #si nombres son iguales, comparo e intercambio notas
                elif Nombres [j] == Nombres [j+1] and Nota[j] < Nota[j+1]:
                    Nota[j], Nota[j+1] = Nota[j+1], Nota[j]

    matriz_nueva = [[Nombres[i], Apellidos[i], Nota[i]] for i in range(n)]
    return matriz_nueva

matriz_nueva = ordenar_nombre_puntos(Apellidos, Nombres, Nota)
print (matriz_nueva)


