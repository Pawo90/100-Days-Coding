from turtle import Turtle, Screen
import random

# Create objec screen
screen = Screen()

# # Create object tim
# tim = Turtle()
# tim.speed(0)
#
# def move_forward():
#     tim.fd(10)
#
# def move_backward():
#     tim.bk(10)
#
# def heading_ccw():
#     tim.left(10)
#
# def heading_cw():
#     tim.right(10)
#
# def reset():
#     screen.resetscreen()
#
#
# # TODO: "W" key - move foward, "S" key - move backward, "A" key - change heading CCW, "D" key - change heading CW, "C" key - cleare screen
#
# screen.onkeypress(move_forward, "w")
# screen.onkeypress(move_backward, "s")
# screen.onkeypress(heading_ccw, "a")
# screen.onkeypress(heading_cw, "d")
# screen.onkeypress(reset, "c")
#
# screen.listen()

# Exit from screen after click

# Creating a multiple turtle objects

# Create turtle race game
# Screen size setup
screen.setup(width=500, height=400)
# Colors for turtles
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turles = []
x_start_pos = -230
y_start_pos = -150
# Creating a list of turles objects
for turle in range(len(colors)):
    # set shape
    turles.append(Turtle(shape='turtle'))
    # set color
    turles[turle].color(colors[turle])
    # set pen up
    turles[turle].penup()
    # set start position
    turles[turle].goto(x_start_pos, y_start_pos)
    # increment y position for next turtle
    y_start_pos += 60

# Popup for user bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Pick color: ")

if user_bet:
    start_race = True

while start_race:

    for turle in range(len(turles)):
        if turles[turle].xcor() >= 220:
            start_race = False
            turtle_winner_name = colors[turle]
        else:
            random_distance = random.randint(0, 10)
            turles[turle].forward(random_distance)


print(f"The winner is: {turtle_winner_name}")
print(f"Your bet: {user_bet}")
if user_bet ==  turtle_winner_name:
    print('You win!')
else:
    print("You lose!")



# Exit from screen after click on it
screen.exitonclick()