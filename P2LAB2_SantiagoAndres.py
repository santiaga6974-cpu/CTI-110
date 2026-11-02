# Andres Santiago
# November 1, 2026
# P2LAB2
# Use a vehicle dictionary to calculate gallons needed for a trip.

# Pseudocode:
# Create a dictionary containing vehicle names and their MPG values.
# Store the dictionary keys in a variable and display them.
# Get a vehicle name from the user and look up its MPG.
# Display the selected vehicle's MPG.
# Get the distance to drive as a float.
# Divide the distance by MPG to calculate gallons needed.
# Display gallons needed with two decimal places.

vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = vehicles.keys()
print(keys)
print()

vehicle = input("Enter a vehicle to see its mpg: ")
mpg = vehicles[vehicle]

print()
print(f"The {vehicle} gets {mpg} mpg.")
print()

miles = float(input(f"How many miles will you drive the {vehicle}? "))
gallons = miles / mpg

print()
print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")
