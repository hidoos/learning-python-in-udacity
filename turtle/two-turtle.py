import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor('#fcfcfc')
    band = turtle.Turtle()
    band.shape("turtle")
    band.color("darkblue")
    band.speed(2)
    band.forward(150)
    band.right(90)
    band.forward(150)
    band.right(90)
    band.forward(150)
    band.right(90)
    band.forward(150)

    angie = turtle.Turtle()
    angie.shape("classic")
    angie.color("red")
    angie.circle(100)

    window.exitonclick()
draw_square()