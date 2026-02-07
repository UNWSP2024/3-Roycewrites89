#Royce Daniel 2/6/2026 "Hot dog vendor"
cost = 0
dog = input("Hot dog or Chili dog? (h/c): ")
if dog == "h":
    cost = 3.50
else:
    cost = 4.50
cheese = input("Cheese? (y/n): ")
if cheese == "y":
    cost += 0.50
peppers = input("Peppers? (y/n): ")
if peppers == "y":
    cost += 0.75
onions = input("Grilled onions? (y/n): ")
if onions == "y":
    cost += 1.00
tax = cost * 0.07
total = cost + tax
print("Cost:", cost)
print("Tax:", tax)
print("Your total's gonna be", total, "Sir")