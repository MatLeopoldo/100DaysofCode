import turtle as t
import random as rd


def draw_shape(num_sides, tim_turtle):
    for _ in range(num_sides):
        tim_turtle.forward(100)
        tim_turtle.right(360 / num_sides)


def random_move(tim_turtle):
    angles = [0, 90, 180, 270]
    tim_turtle.forward(30)
    tim_turtle.setheading(rd.choice(angles))


def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r, g, b)


def draw_spirograph(tim_turtle, step):
    for pos in range(0, 360, step):
        tim_turtle.pencolor(random_color())
        tim_turtle.circle(100)
        tim.setheading(pos)


if __name__ == "__main__":

    tim = t.Turtle()
    t.colormode(255)
    tim.pensize(2)
    tim.speed("fastest")

    draw_spirograph(tim, 5)
    
    screen = t.Screen()
    screen.exitonclick()

