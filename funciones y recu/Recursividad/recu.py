"""def calcular_potencia (base: int = 2 , exponente : int = 2):
    if exponente == 1:
        return base    
    else:
        return (base * exponente) 
resultado3 = calcular_potencia(4,5)

La de arriba NO es recursiva (porque no llama a la funcion."""



def calcular_potencia (base: int = 2 , exponente : int = 2 ) -> int:
    if exponente == 1:
        return base    
    else:
        return base * calcular_potencia (base , exponente -1) 


print (calcular_potencia(4 , 2))

