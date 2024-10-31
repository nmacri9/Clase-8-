from ejercicio1y2 import *
from ejercicio3 import calculadora
from ejercicio4 import perro , gato
from ejercicio5 import Cuenta_Bancaria




libro1 = Libro("ZZZZZ", "Borges", 2000)
libro1.mostrar_informacion()

#2 
rectangulo1 = rectangulo (10 , 5)
rectangulo1.calcular_area()
rectangulo2 = rectangulo (10 , 10)
rectangulo2.calcular_perimetro()

#3
numero1 = calculadora (21, 15)
numero1.sumar()
numero2 = calculadora (10, 10)
numero2.restar()
numero3 = calculadora (12 , 1)
numero3.multiplicar()
numero4 = calculadora (20 , 5)
numero4.dividir()

#4 
perro = perro('Pepe')
gato = gato('Michi')

perro.hacer_sonido()
gato.hacer_sonido()

#5
cuenta = Cuenta_Bancaria("Nico", 7000)
cuenta.saldo__encapsulado()
cuenta.depositar(500)
cuenta.saldo__encapsulado()
cuenta.retirar(300)
cuenta.saldo__encapsulado()
cuenta.retirar(1500)  # retiro con saldo insuficiente