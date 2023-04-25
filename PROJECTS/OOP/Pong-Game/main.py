from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# Control animation - 0 - turn off
# if animation is turned off is needed to update screen manaly with update method in while loop
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()

l_score = Scoreboard((-150, 240))
r_score = Scoreboard((150, 240))

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision to wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision wtih the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
       ball.bounce_x()

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect collision wtih the left paddle and score count
    if ball.xcor() > 350:
        l_score.increase_score()
        ball.reset_position()

    # Ending game
    elif ball.xcor() < -350:
        r_score.increase_score()
        ball.reset_position()

    if l_score.score >= 21 or r_score.score >= 21:
        game_is_on = False

screen.exitonclick()