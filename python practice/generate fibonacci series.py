n=int(input("enter a number:"))

a=0
b=1

print("fibonacci series")

for i in range(n):
    print(a ,end="  ")
    c=a+b
    a=b
    b=c