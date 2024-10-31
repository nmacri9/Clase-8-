nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises",
                    "Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]

Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]


def lista_ordenada(nombres: list, Edades: list)-> list:
    if type(nombres) != list or type(Edades) != list:
        print('No es una lista.')
        return None
    for i in range(len(nombres)):
        for j in range (0, len(nombres)-i-1):
        #comparar el nombre actual con el siguiente
            if nombres[j] > nombres[j+1]:
            # Intercambiar si el nombre  es mayor que el siguiente
                nombres[j], nombres[j+1] = nombres[j+1], nombres[j]
    return nombres

