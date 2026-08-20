from datetime import date

name=input("enter the name:")
age=int(input("enter age:"))

current_year=date.today().year
year_100=current_year+(100-age)


print(f"{name} will 100 year old in the year:{year_100}")