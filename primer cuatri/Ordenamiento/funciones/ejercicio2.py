Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales" , "Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
"Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57]

def ordenar_nombre_puntos(Nombres: list, Puntos: list)-> list:
    if type(Nombres) != list or type(Puntos) != list:
        print('No son una lista.')
        return None
    
    n = len(Nombres)
    
    if n != len(Puntos):
        print('ERROR, no tienen la misma longitud.')
        return None
    for i in range(n):
        for j in range(0, n-i-1):
            
            if Nombres [j] > Nombres[j+1]:
                Nombres[j], Nombres [j+1] = Nombres [j+1], Nombres[j]
                Puntos[j], Puntos[j+1] = Puntos[j+1], Puntos[j]
            
            elif Nombres [j] == Nombres [j+1] and Puntos [j] < Puntos [j+1]:
                Puntos [j], Puntos[j+1] = Puntos[j+1] , Puntos[j]
    
    for i in range(len(Nombres)):
        print(Nombres[i] + ": " + str(Puntos[i]))


print(ordenar_nombre_puntos(Nombres , Puntos))