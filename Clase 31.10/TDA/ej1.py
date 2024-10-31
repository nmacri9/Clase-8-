""" 1- Cargar secuencialmente una lista de alumnos, cada alumno
 debe ser un diccionario con cuatro claves: nombre, apellido, edad y
 la clave curso que posea de valor una tupla con el curso."""

def cargar_alumnos():
    alumnos = []  # Inicializar la lista de alumnos
    
    while True:
        # Solicitar los datos del alumno
        nombre = input("Ingrese el nombre del alumno (o 'salir' para terminar): ")
        if nombre == 'salir':
            break
        
        apellido = input("Ingrese el apellido del alumno: ")
        edad = int(input("Ingrese la edad del alumno: "))
        curso = input("Ingrese el curso del alumno: ")
        
        # Crear un diccionario para el alumno
        alumno = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "curso": (curso, 117)  # Guardar el curso como una tupla
        }
        
        # Agregar el diccionario del alumno a la lista
        alumnos.append(alumno)
        print("Alumno agregado exitosamente.\n")
    
    return alumnos

# Función principal
def main():
    lista_alumnos = cargar_alumnos()
    print("\nLista de alumnos:")
    for alumno in lista_alumnos:
        print(alumno)

if __name__ == "__main__":
    main()
