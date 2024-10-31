#1

def cargar_eventos():
    eventos = []  # Crear la lista de eventos vacía
    continuar = "s"
    indice = 0
    id_evento = 0
    while continuar.lower() == "s":
        print("\nCargando nuevo evento:")
        id_evento += 1
        # Solicitar los datos del evento
        salon_evento = input("Introduce el salon ('San telmo'/ 'Palermo'/'Puerto Madero'): ")
        if salon_evento != 'San telmo' or 'Palermo' or 'Puerto Madero':
            print("ERROR, el salon debe ser:(San telmo'/'Palermo'/'Puerto Madero")
        tipo_evento = input("Introduce el tipo del evento: ")
        if tipo_evento != 'cumpleaÑOS' or 'Bodas de oro' or 'Puerto Madero':
            print("ERROR, el salon debe ser:(San telmo'/'Palermo'/'Puerto Madero")
        # Añadir el evento a la lista manualmente
        if indice == len(eventos):  # Si no hay espacio en la lista
            eventos += [[0, 0, 0]]  # Aumentamos el tamaño de la lista
        # Almacenar el evento en la posición correspondiente
        eventos[indice][0] = id_evento
        eventos[indice][1] = tipo_evento
        eventos[indice][2] = salon_evento

        # Preguntar si desea cargar otro evento
        continuar = input("¿Deseas agregar otro evento? (s/n): ")
        indice += 1  # Incrementar el índice para el siguiente evento

    return eventos

# Llamar a la función para cargar los eventos
eventos_cargados = cargar_eventos()

# Mostrar los eventos cargados
print("Eventos cargados:")
for evento in eventos_cargados:
    print(f"ID: {evento[0]}, Tipo: {evento[1]}, Salón: {evento[2]}")

