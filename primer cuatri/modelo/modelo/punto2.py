from punto1 import *
"""
 2. Calcular por cada salón la cantidad total de fiestas realizadas de cada
 tipo. Utilizar una función.
"""
def contar_fiestas(eventos):
    salones = []
    conteos = []

    for evento in eventos:
        salon, tipo = evento[2], evento[1]

        for i in range(len(salones)):
            if salones[i][0] == salon:  # Encontrar el salón
                for j in range(len(salones[i][1])):
                    if salones[i][1][j] == tipo:  # Encontrar el tipo
                        conteos[i][j] += 1
                        break
                else:
                    salones[i][1] += [tipo]
                    conteos[i] += [1]
                break
        else:
            salones += [[salon, [tipo]]]
            conteos += [[1]]
    # Mostrar resultados
    for i in range(len(salones)):
        print(f"Salón: {salones[i][0]}")
        for j in range(len(salones[i][1])):
            print(f"  {salones[i][1][j]}: {conteos[i][j]}")
