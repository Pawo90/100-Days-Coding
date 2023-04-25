from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 40, "normal")

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"{self.score}", align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()