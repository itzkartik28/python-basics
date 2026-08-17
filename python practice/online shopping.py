amount=int(input("enter purchase amount:"))

if amount>=5000:
    print("free shopping + 20 % dicount")
elif amount>=1000:
    print("free shopping")
else:
    print("shopping charges applicable")