# import colorgram
#
# # Extract 6 colors from an image.
# extracted_colors_list = colorgram.extract('image.jpeg', 30)
#
# colors = []
# for element in range(len(extracted_colors_list)):
#     color = extracted_colors_list[element]
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     touple = (r, g, b)
#     colors.append(touple)

import turtle as turtle_module
import random

color_list = [(225, 233, 229), (225, 156, 74), (36, 98, 143), (160, 21, 46), (19, 52, 85), (227, 208, 101), (128, 184, 208), (223, 78, 51), (180, 44, 84), (142, 98, 42), (49, 56, 105), (206, 128, 157), (43, 137, 49), (124, 196, 141), (101, 12, 52), (80, 25, 19), (58, 180, 128), (205, 91, 106), (151, 212, 174), (146, 207, 222), (137, 180, 45), (28, 157, 171), (83, 73, 40), (9, 79, 115), (227, 181, 160), (95, 102, 165), (220, 174, 186)]


turtle_module.colormode(255)


tim = turtle_module.Turtle()

def set_random_color(color_list):
    color = random.choice(color_list)
    return color

def print_dot(color):
    tim.color(color)
    tim.pendown()
    tim.penup()

def draw_row():
    for _ in range(10):
        tim.dot(20, set_random_color(color_list))
        tim.forward(40)

x_start = -200.0
y_start = -200.0
tim.penup()
tim.goto(x_start, y_start)
for i in range(0, 10):
    draw_row()
    y_start += 40.0
    tim.goto(x_start, y_start)




screen = turtle_module.Screen()
screen.exitonclick()



