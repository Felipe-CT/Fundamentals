class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    """Funcion de la clase Usuario que permite realizar depositos, 
    aumenta el saldo en la cuenta del usuario indicado"""
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    """Funcion de la clase Usuario que permite realizar retiros, 
    reduce el saldo en la cuenta del usuario indicado"""
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    """Funcion de la clase Usuario que permite visualizar el saldo en 
    la cuenta del usuario indicado"""
    def display_user_balance(self):
        print("Usuario :", self.name) 
        print("Saldo: $" , self.account_balance)
        return self

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
        return self

Raul = user("Raul Algo", "RaulA@python.com")
Roberto = user("Roberto Algo", "RobertoA@python.com")
Ramon = user("Ramon Algo", "RamonA@python.com")

Raul.make_deposit(100)
Raul.make_deposit(200)
Raul.make_deposit(50)
Raul.make_withdrawal(8)
Raul.display_user_balance()

Roberto.make_deposit(200)
Roberto.make_deposit(70)
Roberto.make_withdrawal(15)
Roberto.make_withdrawal(23)
Roberto.display_user_balance()

Ramon.make_deposit(600)
Ramon.make_withdrawal(17)
Ramon.make_withdrawal(25)
Ramon.make_withdrawal(79)
Ramon.display_user_balance()

Raul.make_transfer(Ramon, 150)