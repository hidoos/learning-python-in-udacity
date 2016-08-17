import turtle

def draw_tranigle(turtle):
    for i in range(1,4):
        turtle.forward(120)
        turtle.right(120)

def draw_flower():
    brad = turtle.Turtle()
    window = turtle.Screen()
    window.bgcolor("#ccc")
    brad.speed(0.4)
    brad.shape('turtle')
    brad.color('blue')
    for n in range(1, 25):
        brad.right(15)
        draw_tranigle(brad)

    brad.speed(2)
    brad.right(90)
    brad.forward(240)
    window.exitonclick()

draw_flower()