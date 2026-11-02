# Andres Santiago
# November 1, 2026
# P2LAB1
# Calculate and display the diameter, circumference, and area of a circle.

# Pseudocode:
# Import pi from the math module.
# Get the circle's radius from the user as a float.
# Calculate diameter as two times the radius.
# Calculate circumference as two times pi times the radius.
# Calculate area as pi times the radius squared.
# Display diameter, circumference, and area with 1, 2, and 3 decimal places.

import math

radius = float(input("What is the radius of the circle? "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print()
print(f"The diameter of the circle is {diameter:.1f}")
print()
print(f"The circumference of the circle is {circumference:.2f}")
print()
print(f"The area of the circle is {area:.3f}")
