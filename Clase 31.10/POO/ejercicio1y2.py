#1
class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.año_publicacion}")


#2 " 2- Clase para representar un Rectángulo Crear una clase rectángulo que tenga las
#"características base y altura. Del rectángulo se debe poder calcular el área y el perímetro.
#Se debe crear la clase e implementarla"

class rectangulo:
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        self.area = (self.base * self.altura) 
        print(f'El area de un rectangulo es {self.area}')

    def calcular_perimetro(self):
        
        print(f'El perimetro de este rectangulo es {(self.base + self.altura)*2}')
