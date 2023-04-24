import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()

player = Player()

cars = []


def generate_cars(level):
    num_of_cars = random.randint(0, level)
    for _ in range(num_of_cars):
        cars.append(CarManager())


screen.listen()
screen.onkeypress(player.move, "Up")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    generate_cars(scoreboard.score)

    for car in range(len(cars)):
        cars[car].car_move()

    # Detect collision
    for car in range(len(cars)):
        if cars[car].distance(player) < 20:
            print("Collision detected")
            scoreboard.game_over()
            is_game_on = False

    # Detect goal reached
    if player.ycor() >= 280:
        scoreboard.increase_level()
        player.reinitialize()

screen.exitonclick()
