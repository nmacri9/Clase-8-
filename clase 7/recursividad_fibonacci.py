def calcular_fibonacci (n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calcular_fibonacci (n - 1) + calcular_fibonacci (n - 2)
    
print (calcular_fibonacci(6))
# 5 Seria la Posición, no hace ninguna operación.