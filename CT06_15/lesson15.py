print("Hello from lesson 14")

import turtle
windows = turtle.Screen()
windows.setup(width = 500, height = 600 )
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("green")
t.speed(10)



t.goto(-250, 0)
t.setx(250)
t.penup()


t.goto(0, 300)
t.pendown()
t.sety(-300)
# t.seth(0)
# t.pendown()
# t.forward(500)
# t.penup()

# t.goto(0, 300)
# t.seth(270)
# t.pendown()
# t.forward(600)


# for i in range(3, 10):

#     for j in range(i):
#         t.forward(10)
#         t.left(360/i)
windows.mainloop()