from turtle import Turtle

SEGMENT_SIZE = 20
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for segment_num in range(3):
            offset_x = (SEGMENT_SIZE * -1 * segment_num)
            offset_y = 0
            position = (offset_x, offset_y)
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for segment_num in range(len(self.snake_body) - 1, 0, -1):
            new_pos_x = self.snake_body[segment_num - 1].xcor()
            new_pos_y = self.snake_body[segment_num - 1].ycor()
            self.snake_body[segment_num].goto(new_pos_x, new_pos_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)