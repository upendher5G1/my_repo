class BankAccount:
    print("_____ABCD  Bank Of India_____")#class variable
    def __init__(self,name,acc_no,ifsc_code,balance=0):
        self.name=name#instance variable
        self.acc_no= acc_no
        self.ifsc_code=ifsc_code
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return f'deposited {amount} sucessfully\n current balance: {self.balance}'
        else:
            return "deposited unsucessfully"
    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance-=amount
            return f'withdaw {amount} sucessfully\n current balance: {self.balance}'
        else:
             return "withdraw unsucessfully"
    def show_balance(self):
        return f'account holder: {self.name}\naccount number: {self.acc_no}\nifsc code: {self.ifsc_code}\nbalance: {self.balance}'
bank=BankAccount("upendher","123456789","0987654321",100)    #object
while True:
    pin=1234
    enter_pin=int(input("enter your pin: "))
    if pin==enter_pin:
        print("1.deposit\n2.withdraw\n3.show_balance\n4.exit")
    else:
        print("entered incorect pin, try again later!")
        break
    choice=input("enter your choice: ")
    if choice=="1":
        amount=int(input("enter deposit amount:"))
        print(bank.deposit(amount))
        print("deposited sucessfull")
    elif choice=="2":
        amount=int(input("enter withdraw amount:"))
        print(bank.withdraw(amount))
        print("withdraw sucessfull")
    elif choice=="3":
        print("your current balance is",bank.show_balance())
    elif choice=="4":
        break
    else:
        print("entered invalid choice")
       
