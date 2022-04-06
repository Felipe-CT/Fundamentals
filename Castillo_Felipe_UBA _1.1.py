from ast import Return

class CuentaBancaria:
    def __init__(self, tasa_interes,balance):
        self.account_balance = balance
        self.interes= float(1+tasa_interes)

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
    def mostrar_info_cuenta(self,id_cuenta):
        print("Usuario :", self.name) 
        print("Balance: $" , self.cuenta[id_cuenta].account_balance)
        return self

    """Funcion de la clase Usuario que permite realizar transferencias
    de saldo desde un usuario a otro"""
    def make_transfer(self,other_id, other_user, amount):
        if ((amount)<(self.account_balance)):
            self.retiro( amount)
            other_user.cuenta[other_id].deposito( amount)
            print (self)
            print("Has transferido", amount, "a" , other_user.name)
            self.mostrar_info_cuenta()
            other_user.cuenta[other_id].mostrar_info_cuenta()
        else:
            print ("Saldo insuficiente")  
        return self

    """Funcion de la clase Usuario que permite generar interes
    en el saldo de un usuario"""
    def generar_interes(self):
        self.account_balance = self.account_balance*self.interes
        print("su cuenta a generado interes")
        self.mostrar_info_cuenta()
        return self

class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = [CuentaBancaria(tasa_interes=0.02,balance=0)]

    def crear_cuenta(self,tasa,balance):
        if len(self.cuenta)==1:
            print('El usuario ya tiene una cueenta, se creara una segunda cuenta a este usuario')
            self.cuenta.append=[CuentaBancaria(tasa_interes=tasa,balance=balance)]
        elif len(self.cuenta)==2:
            print('El usuario ya tiene dos cuentas, se creara una tercera cuenta')
            self.cuenta.append=[CuentaBancaria(tasa_interes=tasa,balance=balance)]
        if len(self.cuenta)==3:
            print('El usuario no puede tener mas de 3 cuentas.')
        return self

Raul = user('Raul Algo','ra@email.com')
Andres = user('Andres Algo','aa@email.com')

