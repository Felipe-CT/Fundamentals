from ast import Return

class CuentaBancaria:
    def __init__(self, tasa_interes,balance):
        self.account_balance = balance
        self.interes= tasa_interes

    """Funcion de la clase Usuario que permite realizar depositos, 
    aumenta el saldo en la cuenta del usuario indicado"""
    def deposito(self, amount):
        self.account_balance += amount
        return self

    """Funcion de la clase Usuario que permite realizar retiros, 
    reduce el saldo en la cuenta del usuario indicado"""
    def retiro(self, amount):
        if self.account_balance < amount:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.account_balance -= 5
        else:
            self.account_balance -= amount
            return self

    """Funcion de la clase Usuario que permite visualizar el saldo en 
    la cuenta del usuario indicado"""
    def mostrar_info_cuenta(self):
        print("Usuario :", self) 
        print("Balance: $" , self.account_balance)
        return self

    """Funcion de la clase Usuario que permite realizar transferencias
    de saldo desde un usuario a otro"""
    def make_transfer(self, other_user, amount):
        if ((amount)<(self.account_balance)):
            self.retiro(amount)
            other_user.deposito(amount)
            print (self)
            print("Has transferido", amount, "a" , other_user)
            self.mostrar_info_cuenta()
            other_user.mostrar_info_cuenta()
        else:
            print ("Saldo insuficiente")  
        return self

    """Funcion de la clase Usuario que permite generar interes
    en el saldo de un usuario"""
    def generar_interes(self):
        self.account_balance = self.account_balance*(1+self.interes)
        print("su cuenta a generado interes")
        self.mostrar_info_cuenta()
        return self

Raul = CuentaBancaria(0.06,300)
Roberto = CuentaBancaria(0.06,500)


Raul.deposito(100).deposito(200).deposito(50).retiro(8).generar_interes().mostrar_info_cuenta()

Roberto.deposito(200).deposito(70).retiro(15).retiro(23).retiro(23).retiro(23).generar_interes().mostrar_info_cuenta()

