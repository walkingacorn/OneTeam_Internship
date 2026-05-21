class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
        
    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposited {amount}. New balance:{self.__balance}")
        
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdrawn {amount}. Remaining balance:{self.__balance}")
        else:
            print("Insufficient balance")
            
bank_acc_1=BankAccount("A123",1000)
print(bank_acc_1.get_balance())
bank_acc_1.deposit(500)
print(bank_acc_1.get_balance())
bank_acc_1.withdraw(800)
bank_acc_1.withdraw(10000)