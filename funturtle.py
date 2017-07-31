import turtle
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.goto(100,-100)
turtle.goto(100,100)
turtle.goto(-100,100)
turtle.goto(-100,-100)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.shape('turtle')
square= turtle.clone()
square.shape('square')
square.goto(100,100)


triangle = square.clone()
triangle.shape('triangle')
triangle.goto(0,200)
triangle.goto(0,0)
turtle.penup()
square.penup()
square.goto(150,150)
square.stamp()
turtle.goto(200,200)

turtle.mainloop
