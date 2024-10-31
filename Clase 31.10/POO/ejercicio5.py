"""
5- Encapsulamiento Crear una clase Cuenta Bancaria que tenga las características titular y
 saldo encapsulado. De la cuenta bancaria se puede obtener el saldo, depositar o retirar (en
 cada caso imprimir que fue exitoso). Se debe crear la clase e implementarla.
"""

class Cuenta_Bancaria:
    def __init__(self, titular , saldo):
        self.titular = titular
        self.__saldo = saldo

    def saldo__encapsulado (self):
        print(f'Saldo actual : {self.__saldo}')
    
    def depositar (self , deposito):
        if deposito > 0:
            self.__saldo += deposito
            print(f'El deposito es de: {deposito}')
        else:
            print(f'Error, no hay ningun dinero para depositar.')
    
    def retirar (self , retiro):
        if 0 < retiro <= self.__saldo:
            self.__saldo -= retiro
            print(f"Retiro de {retiro} exitoso.")
        else:
            print("Saldo insuficiente o cantidad inválida para el retiro.")

