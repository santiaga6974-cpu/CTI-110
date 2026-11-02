#Andres Santiago
#November 1, 2026
#P3HW1
#Debug a program that summarizes six module grades and displays a letter grade.

# Pseudocode:
# Read six module grades as floats using separate variables.
# Store all six grades in a list.
# Calculate the lowest, highest, sum, and average of the grades.
# Display the aligned statistics with the average to two decimal places.
# Use the average to select A for 90 or above, B for 80 or above,
# C for 70 or above, D for 60 or above, and F otherwise.
# Display the selected letter grade.

# Enter grades for six modules.
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add all six grades to a list and calculate the statistics.
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

print()
print('------------Results------------')
print(f"{'Lowest Grade:':<20}{low}")
print(f"{'Highest Grade:':<20}{high}")
print(f"{'Sum of Grades:':<20}{total}")
print(f"{'Average:':<20}{avg:.2f}")
print('----------------------------------------')

# Determine the letter grade using the unrounded average.
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
