
class CheckingAccount:
    x = 0
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.accountNumber = CheckingAccount.x + 1
        CheckingAccount.x = CheckingAccount.x + 1
        self.__balance = 0
    
    def debit(self, debAmount):
        self.__balance = self.__balance - debAmount
        
    def credit(self, credAmount):
        self.__balance = self.__balance + credAmount
        
    def getBalance(self):
        print("The balance for account number", self.accountNumber, " is: ", self.__balance)
        
def main():
    p1 = CheckingAccount("Sean", "Dunn")
    p2 = CheckingAccount("Pierre", "Dunn")
    
    p1.debit(100)
    p1.credit(350)
    p2.credit(100)
    p2.credit(400)
    p2.debit(155)
    
    p1.getBalance()
    p2.getBalance()
    
    
main()