# Name: Andres Santiago
# Date: November 7, 2026
# Assignment: P4LAB2
# Description: Display multiplication tables and allow repeated runs.
#
# Pseudocode:
# 1. Display the student's name and assignment title.
# 2. Set the run-again response to yes to begin the while loop.
# 3. While the response is yes:
#    a. Ask the user for an integer and convert the input to int.
#    b. If the integer is zero or positive, use a for loop to
#       multiply it by each value from 1 through 12 and display results.
#    c. Otherwise, display that negative values are not accepted.
#    d. Ask whether the user wants to run again (yes or no).
#       Remove extra spaces and convert the response to lowercase.
# 4. When the response is no, leave the loop and display an exit message.

print("Andres Santiago - P4LAB2")

run_again = "yes"

while run_again == "yes":
    number = int(input("\nEnter an integer: "))

    if number >= 0:
        print()
        for multiplier in range(1, 13):
            print(f"{number} * {multiplier} = {number * multiplier}")
    else:
        print("Negative values are not accepted.")

    run_again = input("\nWould you like to run the program again? ").strip().lower()

print("\nExiting program...")
