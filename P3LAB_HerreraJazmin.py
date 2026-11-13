# Jazmin Herrera
# 11/13/2026
# P3LAB
# Change calculator

# prompting for money input 

money = float(input("Enter the amount of money as a float: $"))

print(f"Change amount: {money}")

# converting float to integer to make every amount entered a whole number

money = int(money * 100)

print(f"Change amount: {money}") 

# converting the amount of money into their respective coins

dollars = money // 100
money = money - (dollars * 100)

quarters = money // 25
money = money - (quarters * 25)

dimes = money // 10
money = money - (dimes * 10)

nickels = money // 5
money = money - (nickels * 5)

pennies = money // 1
money = money - (pennies * 1)

# printing amount of change needed

if dollars > 0:
    if dollars == 1:
        print(f"{dollars} Dollar")
    else: 
        print(f"{dollars} Dollars")

if quarters > 0:
    if quarters == 1:
        print(f"{quarters} Quarter")
    else:
        print(f"{quarters} Quarters")

if dimes > 0:
    if dimes == 1:
        print(f"{dimes} Dime")
    else:
        print(f"{dimes} Dimes")

if nickels > 0:
    if nickels == 1:
        print(f"{nickels} Nickel")
    else:
        print(f"{nickels} Nickels")

if pennies > 0:
    if pennies == 1:
        print(f"{pennies} Penny")
    else:
        print(f"{pennies} Pennies")
