text=input("enter a string:")

count=0

for ch in text:
    if ch in "aeiouAEIOU":
        count=count+1

print(f"count vowel:{count}")