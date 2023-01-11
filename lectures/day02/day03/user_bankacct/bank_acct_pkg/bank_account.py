class BankAccount:
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.type = "savings"
        
    def deposit(self, amount):
        self.balance += amount
        
        
    