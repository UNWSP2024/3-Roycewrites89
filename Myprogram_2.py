#Royce Daniel 2/6/2026 "age range calculater"
age = float(input("enter age:"))
if age <= 1:
    print("you are a baby")

if age > 1 and age < 13:
    print("You are a kid")

if age >= 13 and age < 20:
    print("You are a teenager")

if age >= 20:
    print("You are an adult")

