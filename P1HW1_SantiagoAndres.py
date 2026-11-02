# Andres Santiago
# November 1, 2026
# P1HW1
# Calculate an exponent and add and subtract integers entered by the user.

print("-----Calculating Exponents----")
print()
print()

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
power = base ** exponent

print()
print()
print(base, "raised to the power of", exponent, "is", power, "!!")

print()
print()
print("-----Addition and Subtraction----")
print()
print()

starting_integer = int(input("Enter a starting integer: "))
integer_to_add = int(input("Enter an integer to add: "))
integer_to_subtract = int(input("Enter an integer to subtract: "))
result = starting_integer + integer_to_add - integer_to_subtract

print()
print()
print(starting_integer, "+", integer_to_add, "-", integer_to_subtract,
      "is equal to", result)
