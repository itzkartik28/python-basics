num=int(input("enter a number:"))

count=0

while num>0:
    count=count+1
    num=num//10

print(f"the number of digits is:{count}")