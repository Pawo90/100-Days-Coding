from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car = 0
        self.create_car((280, self.draw_ycor()))

    def create_car(self, position):
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.setheading(180)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(position)

    def draw_ycor(self):
        y_cor = []
        for step in range(-240, 260, 20):
            y_cor.append(step)
        new_ycor = random.choice(y_cor)
        return new_ycor

    def car_move(self):
        self.forward(20)
