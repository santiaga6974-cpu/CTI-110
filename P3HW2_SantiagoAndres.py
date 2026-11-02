# Andres Santiago
# November 1, 2026
# P3HW2
# Calculate an employee's regular pay, overtime pay, and gross pay.

# Pseudocode:
# Ask for the employee name, hours worked, and hourly pay rate.
# Convert hours and pay rate to floats.
# If hours worked exceed 40, calculate overtime hours and time-and-a-half pay.
# In that branch, calculate regular pay for 40 hours.
# Otherwise, set overtime hours and pay to zero and pay all hours normally.
# Add regular pay and overtime pay to calculate gross pay.
# Display the employee name and an aligned table of hours and pay.

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0.0
    overtime_pay = 0.0
    regular_pay = hours_worked * pay_rate

gross_pay = regular_pay + overtime_pay

print("-------------------------------------")
print("Employee name:  ", employee_name)
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay'}")
print("-" * 95)
print(f"{hours_worked:<15}{pay_rate:<12}{overtime_hours:<12}{overtime_pay:<20.2f}${regular_pay:<19.2f}${gross_pay:.2f}")
