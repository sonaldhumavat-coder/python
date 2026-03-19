import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(300,400)
pen=turtle.Turtle()
sides=12
lenght=23
angle=360.0/sides
for i in range(sides):
    pen.forward(lenght)
    pen.right(angle)
turtle.done()

