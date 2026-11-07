# P4LAB1 - Turtle House
# Name: Andres Santiago
# Course: CTI-110-2901.2026FA
# Description: Draw a house using a for loop and a while loop.
#
# Pseudocode:
# 1. Set the background color and turtle color.
# 2. Move to the bottom-left corner of the house.
# 3. Use a for loop to draw four sides of a square.
# 4. Move to the top-left corner of the square.
# 5. Use a while loop to draw three sides of a triangle roof.
# 6. Keep the window open until clicked.

import turtle

screen = turtle.Screen()
screen.title("P4LAB1 - Turtle House")
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.shape("turtle")
pen.color("darkblue")
pen.pensize(3)
pen.speed(3)

# Position the turtle at the bottom-left corner.
pen.penup()
pen.goto(-100, -100)
pen.pendown()

# Draw a square with a for loop.
for side in range(4):
    pen.forward(200)
    pen.left(90)

# Position the turtle at the top-left corner.
pen.penup()
pen.goto(-100, 100)
pen.setheading(0)
pen.pendown()

# Draw a triangle roof with a while loop.
side = 0
while side < 3:
    pen.forward(200)
    pen.left(120)
    side += 1

screen.exitonclick()
