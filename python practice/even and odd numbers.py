numbers=[10,30,40,50,60,15,30,35]

even=[]
odd=[]

for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)


print(f"even numbers:{even}")
print(f"even numbers:{odd}")