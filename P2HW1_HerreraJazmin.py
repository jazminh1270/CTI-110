# Jazmin Herrera
# 11/6/2026
# P2HW1 
# Formatting Budget Calculator

print("This program will calculate and display your travel expenses")
print()

base = float(input("Enter your budget: "))
print()

destination = input("Enter your travel destination: ")
print()

num1 = float(input("How much will you likely spend on gas? "))
print()

num2 = float(input("How much will you need for a hotel? "))
print()

num3 = float(input("How much will you need for food? "))
print()

print("--------Travel Expenses--------")

print(f'{"Location:":<15} {destination}')
print(f'{"Initial Budget:":<15} ${base:.2f}')
print(f'{"Fuel:":<15} ${num1:.2f}')
print(f'{"Hotel:":<15} ${num2:.2f}')
print(f'{"Food:":<15} ${num3:.2f}')

print("----------------------------")
sum = base - (num1 + num2 + num3)

print(f'{"Remaining Balance:":<15} ${sum:.2f}')