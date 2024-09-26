import math
# 1A
def perimetro_circulo(radio=3):
        return 2 * math.pi * radio 

area = perimetro_circulo()

print(f'El perimetro de un circulo predeterminado es {area}.')

radio_recibido = (4)
perimetro_recibido = perimetro_circulo(radio_recibido)
print(F'El perimetro del circulo es {perimetro_recibido}')

# 1B
def perimetro_cuadrado(lado: float) -> float:
    calculo = (lado * 4)
    print (f'el perimetro de un cuadrado es {calculo}')
perimetro_cuadrado (5)

#1C
def perimetro_triangulo (lado1 : float , lado2 : float , lado3 : float ) -> float:
    calculo_triangulo = (lado1 + lado2 + lado3)
    print (f'El perimetro de un triangulo es {calculo_triangulo}.')
perimetro_triangulo (6 , 4 , 10)
