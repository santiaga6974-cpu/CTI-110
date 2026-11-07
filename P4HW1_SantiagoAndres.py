# Andres Santiago
# November 7, 2026
# P4HW1
# Collect scores, drop the lowest score, and display an average and grade.
#
# Pseudocode:
# 1. Display the student's name and assignment.
# 2. Ask how many scores the user wants to enter.
# 3. While the number is less than two, ask again so at least one
#    score remains after dropping the lowest score.
# 4. Create an empty list named scores.
# 5. Use a for loop to collect the requested number of scores.
#    a. Ask for the next score.
#    b. While the score is below 0 or above 100, display an error
#       and ask for that same score again.
#    c. Add the valid score to the scores list.
# 6. Find and save the lowest score, then remove it once from the list.
# 7. Divide the sum of the remaining scores by the number remaining.
# 8. Assign A for 90 or higher, B for 80 or higher, C for 70 or higher,
#    D for 60 or higher, and F for averages below 60.
# 9. Display the lowest score, modified list, average, and letter grade.

print("Andres Santiago - P4HW1")

number_of_scores = int(input("\nHow many scores do you want to enter? "))

while number_of_scores < 2:
    print("Enter at least 2 scores so one remains after dropping the lowest.")
    number_of_scores = int(input("How many scores do you want to enter? "))

scores = []

for score_number in range(1, number_of_scores + 1):
    score = float(input(f"Enter score #{score_number}: "))

    while score < 0 or score > 100:
        print("\nINVALID score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{score_number} again: "))

    scores.append(score)

lowest_score = min(scores)
scores.remove(lowest_score)
average = sum(scores) / len(scores)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\n--------------Results--------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("-----------------------------------")
