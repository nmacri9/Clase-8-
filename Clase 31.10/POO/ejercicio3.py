class calculadora:
    def __init__(self, a,b ):
        self.a = a
        self.b = b

    def sumar(self):
        print(f'La suma de los numeros es {self.a + self.b}')

    def restar(self):
        print(f'La resta de los numeros es {self.a - self.b}')

    def multiplicar(self):
        print(f'La multiplicacion de los numeros es {self.a * self.b}')

    def dividir(self):
        if self.b != 0:
            print(f'La division de los numeros es {self.a / self.b}')
        else:
            return "Error: División por cero no permitida"


numero1 = calculadora (21, 15)
numero1.sumar()
numero2 = calculadora (10, 10)
numero2.restar()
numero3 = calculadora (12 , 1)
numero3.multiplicar()
numero4 = calculadora (20 , 5)
numero4.dividir()