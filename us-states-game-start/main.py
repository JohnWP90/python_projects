import turtle
import pandas as pd
from states_names import Names

screen = turtle.Screen()
screen.title("U.S. States Game")

# Names turtle
name = Names()

# Image path.
image = "blank_states_img.gif"

# Create a screen with the image shape.
screen.addshape(image)
turtle.shape(image)

# Function to get coordinates on turtle screen.
"""
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
"""
data = pd.read_csv("50_states.csv")
print(data.loc[5, "state"])
score = 0
correct_guesses = []
while len(correct_guesses) < 50:
    #screen.title(f"U.S. States Game {score}/50")

    # Answer
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States correct", prompt="What's another state's name?")
    answer_state = ' '.join(word.capitalize() for word in answer_state.split())

    if answer_state == "Exit":
        # States to learn csv
        missing_states = [state for state in data.state.to_list() if state not in correct_guesses]
        #missing_states = []
        #for state in data.state.to_list():
        #    if state not in correct_guesses:
        #        missing_states.append(state)
        missing_states_series = pd.Series(missing_states)
        missing_states_series.to_csv("Missing_States.csv")
        break

    if answer_state in data.loc[:, "state"].to_list() and answer_state not in correct_guesses:
        x = data.loc[data.state == answer_state, "x"].to_list()[0]
        y = data.loc[data.state == answer_state, "y"].to_list()[0]

        name.show_state(answer_state, x, y)
        score += 1
        correct_guesses.append(answer_state)




screen.exitonclick()