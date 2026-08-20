salary=int(input("enter salary:"))
experince=int(input("enter experience(years):"))

if salary>=30000 and experince>=5:
    print("bonas=rs.10,000")
elif salary>=30000:
    print("bonus=rs.5000")
else:
    print("no bonus")