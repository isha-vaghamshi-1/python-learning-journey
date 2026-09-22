# Create Account class with 2 attributes - balance & account no Create methods for debit, credit & printing the balance.


class Bank:
    def __init__(self, balance, accNo):
        self.balance = balance
        self.accNo = accNo

    def debit(self,amount):
        self.balance -= amount    

    def credit(self,amount):
        self.balance += amount

    def printing(self):
        print(self.balance)


bank = Bank(200, '35347389363')
bank.debit(50)
bank.credit(30)
bank.printing()




