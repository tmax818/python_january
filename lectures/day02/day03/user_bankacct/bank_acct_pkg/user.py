from bank_acct_pkg.bank_account import BankAccount

class User:
    def __init__(self, name, email, checking = None, savings = None, c_int_rate = 0, s_int_rate = 0):
        self.name = name
        self.email = email
        self.accounts = {}
        if checking:
            self.accounts['checking'] = BankAccount(c_int_rate, balance=0)
        if savings:
            self.accounts['savings'] = BankAccount(s_int_rate, balance=0)
    
    # other methods

    def open_account(self, type):
        pass
    
    def make_deposit(self, amount):
        self.accounts['savings'].deposit(amount)
    

