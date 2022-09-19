import turtle

turtle.fillcolor('red')
turtle.begin_fill()
for x in range(8):
    turtle.forward(50)
    turtle.right(45)
turtle.end_fill()

turtle.penup()
turtle.forward(200)
turtle.pendown()


turtle.fillcolor('yellow')
turtle.begin_fill()
for x in range(8):
    turtle.forward(50)
    turtle.right(45)
turtle.end_fill()

turtle.penup()
turtle.right(90)
turtle.forward(200)
turtle.pendown()

turtle.fillcolor('blue')
turtle.begin_fill()
for x in range(10):
    turtle.forward(50)
    turtle.right(45)
turtle.end_fill()

turtle.penup()

turtle.forward(200)
turtle.pendown()

turtle.fillcolor('purple')
turtle.begin_fill()
for x in range(8):
    turtle.forward(50)
    turtle.right(45)
turtle.end_fill()




turtle.exitonclick()

