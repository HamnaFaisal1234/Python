from turtle import*
bgcolor("black")
pensize(3)
speed(0)
c=["yellow","green" , "red" , ]
for i in range(500):
    color(c[i%3])
    forward(i*4)
    right(121)