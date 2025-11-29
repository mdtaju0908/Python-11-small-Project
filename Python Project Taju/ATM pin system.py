balance= 12000
pin=2121

attempts=0
while attempts < 3 :
    user_pin=int(input("enter the pin :"))
    if user_pin==pin :
        print(" your balance is :",balance)
        amount=int(input("the amount for withdrawl :"))
        balance-=amount
        print("congrats you withdrwed the amount :")
        print("new balance is :",balance)
        break 
    else : 
        print("the input is invalid :")
        attempts +=1

    if attempts == 3:
        print("your access is denied :")