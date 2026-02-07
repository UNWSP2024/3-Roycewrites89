#Royce Daniel. 1/30/2026 "Age calculator"
#Collect age input from user five times
#set the total as the combined value of all ages
#divide the total by five to get the average
#display the average
age1 = int(input("Enter the age of friend 1: "))
age2 = int(input("Enter the age of friend 2: "))
age3 = int(input("Enter the age of friend 3: "))
age4 = int(input("Enter the age of friend 4: "))
age5 = int(input("Enter the age of friend 5: "))
total= age1 + age2 + age3 + age4 + age5
average = total / 5
print("your friends' average age is")
print(f"{average:.2f}")