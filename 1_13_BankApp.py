class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def display_details(self):
        print(f"Account Number: {self.account_number}, Holder Name: {self.holder_name}, Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0.0):
        super().__init__(account_number, holder_name, balance)

class CheckingAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0.0):
        super().__init__(account_number, holder_name, balance)

savings_account = SavingsAccount("12345", "Nihal", 1000)
checking_account = CheckingAccount("67890", "Anshad", 500)

savings_account.display_details()
checking_account.display_details()

savings_account.deposit(200)
savings_account.withdraw(150)
savings_account.display_details()

checking_account.deposit(300)
checking_account.withdraw(700)
checking_account.display_details()
