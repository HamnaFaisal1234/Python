import turtle

turtle.Screen().bgcolor("black")

sc=turtle.Screen()

sc.setup(400,300)

turtle.title("welcome everyone!!!")

board=turtle.Turtle()

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

board.speed('fastest')

board.hideturtle()

while True:

  for x in range(200):

   board.pencolor(colors[x%len(colors)])

   board.width(x/100 + 1)

   board.forward(x)

   board.left(59)

   board.right(239)
  for x in range(200, 0, -1):

   board.pencolor('black')

  board.width(x/100 + 7)

  board.forward(x)

  board.right(59)