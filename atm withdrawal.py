balance=5000
amount=int(input("enter withdrawal amount:"))

if amount>balance:
    print("insufficient balance")
elif amount%100 !=0:
    print("amount shounld be multiple by 100")

else:
    print("transaction successful")