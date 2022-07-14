class ATM(object):
    def __init__(self,userName,pinNo,cardNo,balance):
        self.userName = userName
        self.pinNo = pinNo
        self.cardNo = cardNo 
        self.balance = balance      
    
    def withdrawCash(self,amount):
        newBalance = self.balance
        newBalance = newBalance - amount
        self.balance = newBalance
        print(amount,"was withdrawn from your account") 
        print("Final balance: ",self.balance)

    def changePin(self,newPin):
        self.pinNo = newPin
        print("Your pin was changed to: ",self.pinNo)

newUser = ATM("Kanav",123,12345,10000)

def main():

    a = int(input("Enter pin:"))
    if a == newUser.pinNo:
        print("Please enter action: ")
        action = int(input("1.Check balance or Withdraw cash 2.Change your pin."))
            
        if action == 1:
            amount = int(input("Enter the amount to be withdrawn: "))
            newUser.withdrawCash(amount)

        elif action == 2:
            newPin = int(input("Enter new pin: "))
            newUser.changePin(newPin)
    else:
        print("Invalid pin entered!")

if __name__ == '__main__':
    main()