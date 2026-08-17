age=int(input("enter a age:"))
fitness=input("fitness passed(yes/no):")


if age<=25 and fitness=="yes":
    print("selected !!")

elif age > 25:
    print("rejected-age limit exceeded")

else:
    print("rejected-fitness failed")