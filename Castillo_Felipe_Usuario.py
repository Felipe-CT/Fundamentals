class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    """Funcion de la clase Usuario que permite realizar depositos, 
    aumenta el saldo en la cuenta del usuario indicado"""
    def make_deposit(self, amount):
        self.account_balance += amount

    """Funcion de la clase Usuario que permite realizar retiros, 
    reduce el saldo en la cuenta del usuario indicado"""
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    """Funcion de la clase Usuario que permite visualizar el saldo en 
    la cuenta del usuario indicado"""
    def display_user_balance(self):
        print("Usuario :", self.name) 
        print("Saldo: $" , self.account_balance)

    """Funcion de la clase Usuario que permite realizar transferencias
    de saldo desde un usuario a otro"""
    def make_transfer(self, other_user, amount):
        if ((amount)<(self.account_balance)):
            self.make_withdrawal(amount)
            other_user.make_deposit(amount)
            print (self.name)
            print("Has transferido", amount, "a" , other_user.name)
            self.display_user_balance()
            other_user.display_user_balance()

        else:
            print ("Saldo insuficiente")  

Raul = user("Raul Algo", "RaulA@python.com")
Roberto = user("Roberto Algo", "RobertoA@python.com")

