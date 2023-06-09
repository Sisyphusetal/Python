class BankAccount:

    all_accounts = []

    def __init__(self, balance, interest_rate):
        self.balance = 0 + balance
        self.interest_rate = interest_rate/100
        self.all_accounts.append(self)


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"'Balance: ' {self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance*self.interest_rate
        return self
    
    @classmethod
    def all_accounts_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum

account1 = BankAccount(2000, 1)
account2 = BankAccount(4000, 1)

account1.deposit(200).deposit(300).deposit(200).withdraw(100).yield_interest().display_account_info()
account2.deposit(300).deposit(100).withdraw(100).withdraw(100).withdraw(200).withdraw(100).yield_interest().display_account_info()

print(BankAccount.all_accounts_balances())