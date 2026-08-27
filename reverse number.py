num=int(input("enter a number:"))

reverse=0

while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10

print(f"reverse number is:{reverse}")