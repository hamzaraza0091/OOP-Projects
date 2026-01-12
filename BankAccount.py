class BankAccount:
    def __init__(self,name,account_number,balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        if amount >= 0:
            self.balance = amount
            print(f"Rs: {self.balance} Has been Credit to Your BankAccount.")
        
        else:
            print(f"Invalid Deposit Amount.")

    def withdraw(self,amount):
        if amount <= 0:
            print(" Insufficient balance.")
        elif amount < 0:
            print(" Invalid Withdrawn amount.")
        else:
            self.balance -= amount
            print(f"Rs: {amount} Has Succesfully withdrawn from your BankAccount.")

    def show_balance(self):
        print(f"Your Current Balance is Rs: {self.balance}.")


account1= BankAccount("Hamza","PK1234**********",15000)
account2= BankAccount("HamzaRaza","PK1234**********",12000)


account1.deposit(15000)
account1.withdraw(9500)
account1.show_balance()
print()
account2.deposit(12000)
account2.withdraw(7500)
account2.show_balance()