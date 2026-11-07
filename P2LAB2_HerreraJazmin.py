# Jazmin Herrera
# 11/6/2026
# P2LAB2
# Dictionary 

cars = {'Toyota':25.8, 'Audi':21.5, 'Genesis':21.2, 'Honda':28.7}

cars_keys = cars.keys ()

print(cars_keys)

print(*cars_keys, sep = ", ")

car_name = input("Enter a vehicle: ")

car_mpg = cars[car_name]
print(f"The {car_name} has a miles per gallon of {car_mpg}")

miles_driven = float(input(f"How many miles will you drive your {car_name}? "))

gallons_used = miles_driven/car_mpg 

print(f"{gallons_used:.2f} gallons of gas needed to drive your {car_name} {miles_driven} miles.")