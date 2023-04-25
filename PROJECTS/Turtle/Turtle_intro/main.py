import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
#tim.shape("turtle")


def draw_dash_line():
        for _ in range(2):
            tim.pendown()
            tim.forward(2)
        for _ in range(2):
            tim.penup()
            tim.forward(2)


screen = Screen()

def draw_shape(num_sides, side_lenght):
    FULL_ANGLE = 360
    angle = FULL_ANGLE / num_sides
    for _ in range(num_sides):
        tim.forward(side_lenght)
        tim.right(angle)

def draw_n_shapes(num_of_shapes, side_lenght):
    for i in range(3, num_of_shapes):
        draw_shape(i, side_lenght)

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, b, g)
    return color
def random_walk(setps):
    directions = ['fd', 'bk', 'rt', 'lt']
    step_dist = 25
    for _ in range(setps):
        direciion = random.choice(directions)
        if direciion == 'fd':
            tim.forward(step_dist)
        elif direciion == 'bk':
            tim.backward(step_dist)
        elif direciion == 'rt':
            tim.rt(90)
            tim.forward(step_dist)
        elif direciion == 'lt':
            tim.lt(90)
            tim.forward(step_dist)

turtle.colormode(255)
def draw_stereogram(no_of_circles, radius, speed):
    """ no_of_circles => is the number of circles
        radius => is the cicrle radius
        speed => is the drawind speed from 0 to 10
        0 - fastests
        1 - slow
        10 - fast
    """
    FULL_ANGLE = 360
    angle = FULL_ANGLE / no_of_circles
    for _ in range(no_of_circles):
        tim.speed(speed)
        tim.color(random_color())
        tim.circle(radius)
        tim.rt(angle)

draw_stereogram(150, 100, 0)



# directions = [tim.fd(50), tim.bk(50), tim.lt(90), tim.rt(90)]
tim.lt(90)



# Screen exit
screen_exit = screen.exitonclick()

