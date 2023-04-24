from turtle import Turtle

INITIAL_POSITION = (-280, 260)
ALIGNMENT = "left"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.color("green")
        self.hideturtle()
        self.goto(INITIAL_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)

    def increase_level(self):
        self.score += 1
        self.update_scoreboard()
