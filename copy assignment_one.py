import turtle
for x in range(4):
    turtle.fillcolor('red')
    turtle.begin_fill()
    for x in range(8):
        turtle.forward(100)
        turtle.right(45)
    turtle.end_fill()
turtle.penup()
turtle.forward(200)
    turtle.pendown()


turtle.exitonclick()

