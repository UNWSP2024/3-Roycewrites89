#Royce Daniel 2/6/2026 "Shipping company shenanigans"
weight = float(input("Enter package weight (in pounds): "))
if weight <= 2:
    cost = weight * 1.50
elif weight <= 6:
    cost = weight * 3.00
elif weight <= 10:
    cost = weight * 4.00
else:
    cost = weight * 4.75

print("Shipping cost:", cost)
