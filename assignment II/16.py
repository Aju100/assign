from random import randint
class Customer:
    def __init__(self,name):
        self.name = name
        self.account_balance = 0

    def create_account(self):
        account_id = randint(100000,999999)
        self.account_id = account_id
        print(
            "Account {} is created for {}".format(self.account_id,self.name)
        ) 

    def deposit(self,amount):
        self.account_balance += amount
        print(
            "{} has deposited {}".format(self.name,self.account_balance)
        )
    
    def withdraw(self,amount):

        self.account_balance -= amount
        print(
            "{} has left {}".format(self.name,self.account_balance)
        ) 
        self.account_balance = amount
        print(
            "{} has withdraw {}".format(self.name,self.account_balance)
        )
    

a = Customer("Aju")
a.create_account()
a.deposit(1000)
a.withdraw(300)
