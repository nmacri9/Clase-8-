#8 
def calcular_salario( horas_trabajadas: float , antiguedad : int )-> float: 
    """Calcular salario cantidad de horas trabajadas multiplicadas por 10 y un
    incremento del 3% por cada año de antigüedad"""
    salario_base = horas_trabajadas * 10
    aumento = salario_base * (antiguedad * 0.03)
    salario_aumentado = salario_base + aumento
    return salario_aumentado

salario = calcular_salario(40,5)

def calcular_productividad( horas_trabajadas: float , artef_producidos: int ) -> float : 
    """calcule la productividad del empleado. La
    misma se calcula como la cantidad de artefactos producidos, dividido por la cantidad de
    horas de trabajo"""
    productividad = (artef_producidos / horas_trabajadas)
    return productividad

def datar_empleado (nombre: str , edad: int ,  horas_trabajadas, antiguedad,):
    """toda la información del empleado incluyendo la calculada en 
    las dos funciones anteriores, nombre y edad."""
    reporte = (f""" Reporte del empleado: 
        Nombre {nombre}
        Edad: {edad}
        Horas trabajadas: {horas_trabajadas}
        Antiguedad: {antiguedad}
        Salario: {salario} """)
    return reporte

reporte = datar_empleado ("Nico" , 20 , 50, 5)
print (reporte)

