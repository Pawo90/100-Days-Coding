from turtle import Turtle
import random

FOOD_POS_MAX_POSITIV = 270
FOOD_POS_MAX_NEGATIV = -270

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(FOOD_POS_MAX_NEGATIV, FOOD_POS_MAX_POSITIV)
        random_y = random.randint(FOOD_POS_MAX_NEGATIV, FOOD_POS_MAX_POSITIV)
        self.goto(random_x, random_y)
