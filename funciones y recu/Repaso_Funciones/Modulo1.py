import math
# 1A
def calcular_circulo(radio=3):
        return math.pi * radio ** 2

area = calcular_circulo()

print(f'El area de un circulo predeterminado es {area}.')

radio_recibido = (4)
area_recibida = calcular_circulo(radio_recibido)
print(F'El area del circulo es {area_recibida}')

# 1B
def area_cuadrado(lado: float) -> float:
    calculo = (lado*lado)
    print (f'el area de un cuadrado es {calculo}')
area_cuadrado (5)

#1C
def area_triangulo (base: float , altura : float) -> float:
    calculo_triangulo = (base * altura)
    print (f'El area de un triangulo es {calculo_triangulo}.')
area_triangulo (5 , 6)