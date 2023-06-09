class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}

    def add_account(self, account_name, balance, interest_rate):
        self.accounts[account_name] = BankAccount(balance, interest_rate, account_name)

    def make_deposit(self, amount, account_name):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else:
            print(f"No account named '{account_name} found.")
    
    def make_withdrawal(self, amount, account_name):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print(f"No account named '{account_name} found.")
    
    def display_user_balance(self, account_name):
        if account_name in self.accounts:
            self.accounts[account_name].display_account_info()
        else:
            print(f"No account named '{account_name} found.")
    
    def transfer_money(self, amount, account_name, other_user, other_account_name,):
        if account_name in self.accounts and other_account_name in other_user.accounts:
            self.accounts[account_name].withdraw(amount)
            other_user.accounts[other_account_name].deposit(amount)
        else:
            print("There was an error: one or more accounts not found.")



class BankAccount:

    all_accounts = []

    def __init__(self, balance, interest_rate, account_name):
        self.balance = 0 + balance
        self.interest_rate = interest_rate/100
        self.account_name = account_name
        self.all_accounts.append(self)


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds for this withdrawal, please contact your bank.")
        return self

    def display_account_info(self):
        print(f"Account name: {self.account_name}, Balance: {self.balance}")

    def yield_interest(self, account_name):
        self.balance += self.balance*self.interest_rate
        return self
    
    @classmethod
    def all_accounts_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum
    

user1 = User('Kurt', 'kurt@gmail.com')
user2 = User('Aubrey', 'aubrey@gmail.com')
user1.add_account('Checking', 2000, 0)
user1.add_account('Savings', 3000, 2)
user2.add_account('Checking', 1000, 0)
user2.add_account('Savings', 3500, 2)
user1.make_deposit(200, 'Savings')
user2.make_withdrawal(400, 'Checking')
user1.transfer_money(400, 'Checking', user2, 'Savings')
user1.display_user_balance('Checking')
user1.display_user_balance('Savings')
user2.display_user_balance('Checking')
user2.display_user_balance('Savings')