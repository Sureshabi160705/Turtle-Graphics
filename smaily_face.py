import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")

ms_dhoni = turtle.Turtle()
ms_dhoni.shape("turtle")
ms_dhoni.color("blue")
ms_dhoni.pensize(5)

# Function to draw a circle
def draw_circle(radius, color):
    ms_dhoni.fillcolor(color)
    ms_dhoni.begin_fill()
    ms_dhoni.circle(radius)
    ms_dhoni.end_fill()

# Draw the face
draw_circle(100, "light blue")

# Draw the left eye
ms_dhoni.penup()
ms_dhoni.goto(-40, 120)
ms_dhoni.pendown()
draw_circle(15, "black")

# Draw the right eye
ms_dhoni.penup()
ms_dhoni.goto(40, 120)
ms_dhoni.pendown()
draw_circle(15, "black")

# Draw the mouth
ms_dhoni.penup()
ms_dhoni.goto(-40, 85)
ms_dhoni.pendown()
ms_dhoni.right(90)
ms_dhoni.circle(40, 180)

# Hide the turtle
ms_dhoni.hideturtle()

# Keep the window open
turtle.mainloop()