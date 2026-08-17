salary=int(input("enter salary:"))
cibil=int(input("enter cibil score:"))

if salary>=25000 and cibil>=750:
    print("loan approval")

elif salary <25000:
    print("loan rejected-low salary")

else:
    print("loan rejected-low cibil score")