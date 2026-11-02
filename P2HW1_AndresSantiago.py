# Andres Santiago
# November 1, 2026
# P2HW1
# Calculate travel expenses and display an aligned summary with dollar amounts.

# Pseudocode:
# Display the program description.
# Get the budget and travel destination from the user.
# Get the gas, accommodation, and food expenses from the user.
# Add the three expenses to calculate total expenses.
# Subtract total expenses from the budget to calculate the remaining balance.
# Display the destination and money values in aligned columns.
# Format each money value with a dollar sign and two decimal places.

print("This program calculates and displays travel expenses")
print()

# Convert money inputs to floats so the user can enter dollars and cents.
budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))

# Calculate the total cost and the money left after expenses.
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Use the same label width to align destination and dollar amounts.
print()
print("------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accommodation:':<20}${accommodation:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("----------------------------------------")
print()
print(f"{'Remaining Balance:':<20}${remaining_balance:.2f}")
