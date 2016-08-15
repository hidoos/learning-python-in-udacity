import turtle

turtle_list = [{
    'shape': 'turtle',
    'color': 'darkgreen'
}, {
    'shape': 'arrow',
    'color': 'red'
},{
    'shape': 'triangle',
    'color': 'blue'
}]

def main():
    window = turtle.Screen()
    window.bgcolor("#ccc")
    for single_turtle in turtle_list:
        band = turtle.Turtle()
        draw_mutilple_turtle(
            band, 
            shape = single_turtle['shape'], 
            color = single_turtle['color'])
    window.exitonclick()

def draw_turtle(turtle_instance, shape = "turtle", color = "darkblue"):
    turtle_instance.shape(shape)
    turtle_instance.color(color)
    if shape == 'turtle':
        for times in range(0,4):
            turtle_instance.forward(150)
            turtle_instance.right(90)

    if shape == 'arrow':
        turtle_instance.circle(100)

    if shape == 'triangle':
        turtle_instance.circle(100 * 1.3)

main()
