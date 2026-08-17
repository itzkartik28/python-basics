num=int(input("enter a number:"))

temp=num
reverse=0

while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10

if temp==reverse:
        print("palindrome")
else:
        print("not a palindrome")