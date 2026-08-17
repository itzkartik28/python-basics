username=input("enter username:")
password=int(input("enter password:"))

if username=="student" and password==1234:
    print("welcome student")

elif username=="student":
    print("incorrect password")

else:
    print("user not found")