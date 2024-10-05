class Bankaccount:
    def __init__(self,name,acc_no,balance=0):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance
    def deposit(self,depo):
        self.depo=depo
        if(depo>0):
            self.balance+=depo
            print(f"successfully deposited tk {depo}.New balance is tk {self.balance}")
        else:
            print("Deposit must be positive")
    def withdraw(self,withdr):
        self.withdr=withdr
        if(self.balance<withdr):
            print("Insufficiant balance....")
        elif(withdr<0):
            print("withdraw must be positive")
        else:
            self.balance-=withdr
            print(f"successfully withdraw tk {withdr}.New balance is tk {self.balance}")
    def display(self):
        print("Account name : ",self.name)
        print("Account no : ",self.acc_no)
        print("deposit : ",self.depo)
        print("withdraw : ",self.withdr)
        print("Main Balance : ",self.balance)
c=Bankaccount("Deb",12324)
c.deposit(50000)
c.withdraw(6000)
c.display()
