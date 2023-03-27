from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance):
        self.balance = balance
        
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
class CheckingAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient balance!")
            
class SavingsAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance - amount >= 5000:
            self.balance -= amount
        else:
            print("Insufficient balance!")
            
class BusinessAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance - amount >= 10000:
            self.balance -= amount
        else:
            print("Insufficient balance!")
            
# ATM program
while True:
    print("Enter account type:")
    print("1. Checking Account")
    print("2. Savings Account")
    print("3. Business Account")
    print("4. Exit")
    
    choice = int(input("Enter choice (1-4): "))
    
    if choice == 1:
        account = CheckingAccount(int(input("Enter balance: ")))
        print("Account created successfully!")
        
        while True:
            print("Checking Account")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Go back to main menu")
            
            ch = int(input("Enter choice (1-4): "))
            
            if ch == 1:
                amount = int(input("Enter amount to deposit: "))
                account.deposit(amount)
                print("Amount deposited successfully!")
            elif ch == 2:
                amount = int(input("Enter amount to withdraw: "))
                account.withdraw(amount)
                print("Amount withdrawn successfully!")
            elif ch == 3:
                print("Balance: ", account.balance)
            else:
                break
                
    elif choice == 2:
        account = SavingsAccount(int(input("Enter balance: ")))
        print("Account created successfully!")
        
        while True:
            print("Savings Account")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Go back to main menu")
            
            ch = int(input("Enter choice (1-4): "))
            
            if ch == 1:
                amount = int(input("Enter amount to deposit: "))
                account.deposit(amount)
                print("Amount deposited successfully!")
            elif ch == 2:
                amount = int(input("Enter amount to withdraw: "))
                account.withdraw(amount)
                print("Amount withdrawn successfully!")
            elif ch == 3:
                print("Balance: ", account.balance)
            else:
                break
                
    elif choice == 3:
        account = BusinessAccount(int(input("Enter balance: ")))
        print("Account created successfully!")
        
        while True:
            print("Business Account")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Go back to main menu")
            
            ch = int(input("Enter"))