# Andres Santiago
# November 7, 2026
# P4HW2
# Calculate employee pay and payroll totals for multiple employees.
#
# Pseudocode:
# 1. Display the student's name and assignment.
# 2. Set employee count and all payroll totals to zero.
# 3. Ask for an employee name or exactly Done to finish.
# 4. While the employee name is not exactly Done:
#    a. Ask for the employee's pay rate and hours worked.
#    b. If hours exceed 40, calculate overtime hours as hours minus 40,
#       regular pay as 40 times pay rate, and overtime pay as
#       overtime hours times pay rate times 1.5.
#    c. Otherwise, set overtime hours and overtime pay to zero,
#       and calculate regular pay as hours times pay rate.
#    d. Calculate gross pay as regular pay plus overtime pay.
#    e. Display the employee's name, hours, rate, and pay information.
#    f. Add one to the employee count and add each pay amount
#       to its corresponding running total.
#    g. Ask for the next employee name or exactly Done to finish.
# 5. Display employee count and total overtime, regular, and gross pay.

print("Andres Santiago - P4HW2")

employee_count = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

employee_name = input('\nEnter employee\'s name or "Done" to terminate: ')

while employee_name != "Done":
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    hours_worked = float(input(f"How many hours did {employee_name} work? "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_pay = 40 * pay_rate
        overtime_pay = overtime_hours * pay_rate * 1.5
    else:
        overtime_hours = 0.0
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0.0

    gross_pay = regular_pay + overtime_pay

    print(f"\nEmployee name: {employee_name}\n")
    print("Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay")
    print("-" * 100)
    print(f"{hours_worked:.1f}\t\t{pay_rate:.2f}\t\t{overtime_hours:.1f}\t\t"
          f"${overtime_pay:.2f}\t\t${regular_pay:.2f}\t\t${gross_pay:.2f}")

    employee_count += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    employee_name = input('\nEnter employee\'s name or "Done" to terminate: ')

print(f"\nTotal number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
