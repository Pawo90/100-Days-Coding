import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S. States Game")

# Add new shape a map
image = "blank_states_img.gif"
screen.addshape(image)
# Set new shape on screen
t.shape(image)

# Read data file
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

# A list with guessed states
guessed_states = []

while len(guessed_states) < 50:

    # POPUP
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's").title()
    # SOLUTION 1 - WITH CLASSIC FOR, IF etc. stements
    # if answer_state == "Exit":
    #     missing_states = []
    #     for state in all_states:
    #         if state not in guessed_states:
    #             missing_states.append(state)
    #
    #     new_data = pd.DataFrame(missing_states)
    #     new_data.to_csv("states_to_lern.csv")
    #     break

    # SOLUTION 2 - WITH CLASSIC LIST COMPREHENSION
    if answer_state == "Exit":
        # missing_states = [new_item for item in items if test]
        missing_states = [state for state in all_states if state not in guessed_states]

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_lern.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state = t.Turtle()
        state.hideturtle()
        state.penup()
        state_data = data[data.state == answer_state]
        state.goto(int(state_data.x), int(state_data.y))
        # state.write(answer_state)
        state.write(state_data.state.item())

# states to lern.csv
