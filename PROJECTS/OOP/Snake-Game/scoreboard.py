from turtle import Turtle


# with open(data.txt, mode="w") as data:
#     highscore_data = data.read()

ALIGMENT = "center"
FONT = ("Arial", 15, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.penup()
        self.color('green')
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def write_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score

        with open("data.txt", mode="w") as data:
            #data.write(str(self.highscore))
            # or
            data.write(f"{self.highscore}")

