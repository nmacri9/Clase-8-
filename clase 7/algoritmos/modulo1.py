def buscar_lineal (lista: list, buscado : any):
    for i in range (len(lista)):
        
        if lista [i] == buscado:
        
            return i

    return None

def buscar_binaria(lista: list, buscado : int):

    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        medio = (inicio + final) // 2

        if lista[medio] == buscado:
            return medio
        elif lista[medio] < buscado:
            inicio = medio + 1
        else: 
            lista[medio] > buscado
            final = medio - 1

    return None