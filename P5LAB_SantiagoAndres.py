# Andres Santiago
# November 18, 2026
# P5LAB
# Simulate a self-checkout purchase and print the customer's change.

import random
from math import isfinite


# Pseudocode:
# Generate and display a random purchase total between $0.01 and $100.00.
# Ask for cash until the customer enters a valid amount that covers the total.
# Subtract the total from the cash and display the change owed.
# Convert the change to cents and display the count for each denomination used.


def disperse_change(change):
    cents = int(round(change * 100))
    if cents == 0:
        print("No change")
        return

    denominations = (
        (100, "Dollar", "Dollars"),
        (25, "Quarter", "Quarters"),
        (10, "Dime", "Dimes"),
        (5, "Nickel", "Nickels"),
        (1, "Penny", "Pennies"),
    )
    for value, singular, plural in denominations:
        count = cents // value
        cents -= count * value
        if count > 0:
            print(count, singular if count == 1 else plural)


def main():
    total = round(random.uniform(0.01, 100.00), 2)
    print("Andres Santiago | P5LAB")
    print(f"You owe ${total:.2f}")

    while True:
        try:
            cash = float(input("How much cash will you put in the self-checkout? "))
        except ValueError:
            print("Please enter a valid dollar amount.")
            continue

        if not isfinite(cash) or cash < 0 or cash != round(cash, 2):
            print("Please enter a nonnegative amount with up to two decimal places.")
        elif cash < total:
            print("That does not cover the purchase total. Please try again.")
        else:
            break

    change = round(cash - total, 2)
    print(f"Change is: ${change:.2f}")
    print()
    disperse_change(change)


if __name__ == "__main__":
    main()
