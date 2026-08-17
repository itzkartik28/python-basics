username=input("enter the username:")
password=input("enter the password:")

if username=="admin" and password=="1234":
    print("login successful !!")
elif username=="admin":
    print("wrong password")
else:
    print("invalid username!! try again!")