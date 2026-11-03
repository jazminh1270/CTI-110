# Jazmin Herrera
# 11/2/2026
# P1HW1
# integer input & output

print("----Calcuating Exponents----")
print()

base = int(input("Enter a base number: "))
exponent = int(input("Enter an exponent: "))
result = base ** exponent
print(base, "Raised to the power of", exponent, "is", result, "!!")

print("----Adding & Subtracting----")
print()

num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

sum_result = num1 + num2
final_result = sum_result - num3

print(num1, "+", num2, "-", num3, "is equal to", final_result, "!!")
