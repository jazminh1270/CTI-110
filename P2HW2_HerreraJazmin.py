# Jazmin Herrera
# 11/13/2026
# P2HW2
# Grades prompt

# labelling modules & asking for input

module1 = float(input("Enter your grade for Module 1: "))
module2 = float(input("Enter your grade for Module 2: "))
module3 = float(input("Enter your grade for Module 3: "))
module4 = float(input("Enter your grade for Module 4: "))
module5 = float(input("Enter your grade for Module 5: "))
module6 = float(input("Enter your grade for Module 6: "))
print()

# creating list of grades

grades = [module1, module2, module3, module4, module5, module6]

# getting lowest and highest grades

lowest_grade = min(grades)
highest_grade = max(grades)

# calculating sum and average of grades

grades_sum = sum(grades)
average_grade = grades_sum / len(grades)

# printing results

print("----------Results----------")
print(f'{"Lowest Grade:":<20} {lowest_grade:.2f}')
print(f'{"Highest Grade:":<20} {highest_grade:.2f}')
print(f'{"Sum of Grades:":<20} {grades_sum:.2f}')
print(f'{"Average Grade:":<20} {average_grade:.2f}')
print("------------------------------") 