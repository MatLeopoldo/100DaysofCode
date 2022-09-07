import colorgram as cg
import turtle as t
import random as rd


#def generate_colors():
#    rgb_colors = []
#    colors = cg.extract('image.jpg', 30)
#    for color in colors:
#        r = color.rgb.r
#        g = color.rgb.g
#        b = color.rgb.b
#        rgb_colors.append((r, g, b))
#    
#    return rgb_colors

colors = [(5, 33, 61), (31, 105, 133), (112, 179, 190), (54, 161, 177), (246, 206, 165), (14, 79, 106), 
(219, 160, 136), (128, 193, 187), (195, 145, 152), (248, 213, 128), (240, 170, 154), (152, 209, 201), (123, 85, 108), 
(29, 66, 103), (177, 101, 118), (182, 214, 202), (67, 165, 157), (65, 131, 124), (145, 208, 212), (229, 160, 165), 
(182, 201, 207), (11, 93, 83), (118, 120, 148), (122, 106, 95), (180, 108, 103), (188, 190, 197), (9, 68, 63), 
(50, 31, 51), (79, 53, 77), (134, 134, 112)]


def random_color():
    return rd.choice(colors)


def draw_square_dots(tim_turtle, len_in_dots):
    tim_turtle.home()
    tim_turtle.hideturtle()
    tim_turtle.penup()
    tim_turtle.speed("fastest")

    for _ in range(len_in_dots):
        for _ in range(len_in_dots):
            tim_turtle.pencolor(random_color())
            tim_turtle.dot(20)
            pos_x, pos_y = tim_turtle.pos()
            pos_x += 30
            tim_turtle.setpos(pos_x, pos_y)

        pos_x = 0
        pos_y += 30
        tim_turtle.setpos(pos_x, pos_y)


if __name__ == "__main__":
    t.colormode(255)
    tim = t.Turtle()
    draw_square_dots(tim, 10)

    screen = t.Screen()
    screen.exitonclick()
