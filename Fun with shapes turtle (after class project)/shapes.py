import turtle


screen = turtle.Screen()
screen.bgcolor("black")  
screen.title("Drawing Shapes with Turtle")

# Create the turtle
pen = turtle.Turtle()
pen.speed(2)  

# Function to draw and fill an equilateral triangle
def draw_triangle(side_length, color):
    pen.color(color)
    pen.begin_fill()
    for _ in range(3):
        pen.forward(side_length)
        pen.left(120)
    pen.end_fill()


    #2nd triangle
    # Function to draw and fill an equilateral triangle
def draw_triangle2(side_length, color):
    pen.color(color)
    pen.begin_fill()
    for _ in range(3):
        pen.forward(side_length)
        pen.left(120)
    pen.end_fill()

# Function to draw and fill a rectangle
def draw_rectangle(width, height, color):
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

# Function to draw and fill a hexagon
def draw_hexagon(side_length, color):
    pen.color(color)
    pen.begin_fill()
    for _ in range(6):
        pen.forward(side_length)
        pen.left(60)
    pen.end_fill()

# Positioning and drawing shapes
pen.penup()
pen.goto(-210, 100)  # Position for triangle
pen.pendown()
draw_triangle(100, "purple")  
#2nd triangle
pen.penup()
pen.goto(50, 100)  # Position for triangle
pen.pendown()
draw_triangle2(100, "purple") 

 

pen.penup()
pen.goto(-60, -100)  # Position for hexagon
pen.pendown()
draw_hexagon(70, "white") 

pen.penup()
pen.goto(-120, -210)  # Position for rectangle
pen.pendown()
draw_rectangle(180, 60, "red") 


pen.hideturtle()
turtle.done()