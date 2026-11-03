# Jazmin Herrera
# 11/2/2026
# P1HW2
# User Questions

print("This program will calculate and display your travel expenses")
print()

base = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
num1 = float(input("How much will you likely spend on gas? "))
num2 = float(input("How much will you need for a hotel? "))
num3 = float(input("How much will you need for food? "))


print("----Travel Expenses----")
print()

print("Location: ", destination)
print("Initial Budget: ", base)
print()

print("Fuel: ", num1)
print("Hotel: ", num2)
print("Food: ", num3)

sum = base - (num1 + num2 + num3)

print("Remaining Balance: ", sum)