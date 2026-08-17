age=int(input("enter the age:"))
citizen=input("are you an indian citizen(yes/no):")

if age>=18 and citizen=="yes":
    print("eligiable for voting")
elif age<18:
    print("not eligiable for voting")
else:
    print("not eligiable-not a citizen")