# Jazmin Herrera
# 11/13/2026
# P3HW2
# Employee Pay Calculations

# prompt for employee info

employee = input("Enter employee name: ")
hours = float(input("Enter hours worked: "))
pay_rate = float(input("Enter pay rate: $"))
print("-------------------------------")

# determine if employee worked overtime & determine overtime pay

if hours > 40:
    reg_pay = 40 * pay_rate
    overtime_hrs = hours - 40
    overtime_pay = overtime_hrs * (pay_rate * 1.5)
    gross_pay = reg_pay + overtime_pay
else: 
    overtime_pay = 0
    overtime_hrs = 0
    reg_pay = hours * pay_rate
    gross_pay = reg_pay

# display info

print(f"Employee Name: ", employee)
print()

print(f'{"Hours Worked":<20}{"Pay Rate":<20}{"OverTime":<20}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay":<20}')
print("-----------------------------------------------------------------------------------------------------------------")
print(f'{hours:<20}{pay_rate:<20.2f}{overtime_hrs:<20}{overtime_pay:<20.2f}{reg_pay:<20.2f}{gross_pay:<20.2f}')

