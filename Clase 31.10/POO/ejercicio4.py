"""
4- Herencia de clases
Crear una clase Animal que tenga la característica nombre. La clase Perro que herede de
Animal las características y realice el sonido “guau guau”. La clase Gato que herede de
Animal las características y realice el sonido “Miau”. Del gato y el perro se debe poder
mostrar el sonido que realizan. Se debe crear la clase e implementarla
"""

class animal:
    def __init__(self, nombre :str):
        self.nombre = nombre
    
    def mostrar_nombre(self):
        print(f"Nombre del animal: {self.nombre}")

class perro(animal):
    def hacer_sonido(self):
        self.nombre = 'Pepe'
        self.sonido = 'Guau guau'
        print(f'El nombre del Perro es {self.nombre} y el sonido que hace es {self.sonido}')

class gato(animal):
    def hacer_sonido(self):
        self.nombre = 'Michi'
        self.sonido = 'Miau'
        print(f'El nombre del Gato es {self.nombre} y el sonido que hace es {self.sonido} ')

