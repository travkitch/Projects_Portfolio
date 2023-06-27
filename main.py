import turtle
from turtle import Turtle, Screen
import pandas as pd
from states import States

screen = Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# get csv data as dataframe
data = pd.read_csv("50_states.csv")
list_of_states = data["state"].tolist()
correct_answers = []


game_is_on = True
while game_is_on:

    num_of_correct = len(correct_answers)
    answer_state = screen.textinput(title=f"{num_of_correct}/50 States Correct", prompt="What's another state's name?").title()
    S = States()

# compare if the answer is in the list/ column of state names
    if answer_state == "Exit":
        missing_states = [state for state in list_of_states if state not in correct_answers]
        # missing_states = []
        # for state in list_of_states:
        #     if state not in correct_answers:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in list_of_states:
        correct_answers.append(answer_state)
        list_of_states.remove(answer_state)
        x_for_state = data[data.state == answer_state].x.item()
        y_for_state = data[data.state == answer_state].y.item()
        S.write_on_map(state=answer_state, map_x=x_for_state, map_y=y_for_state)

    if len(correct_answers) == 50:
        game_is_on = False

# TODO 1) Convert user input to title case
# TODO 2) Check if the guess is among the 50 states
# TODO 3) Write correct guesses on map
# if answer_state in list_of_states:
# to get each row: data[data["state"] == "Colorado"])
# x = data[data["state"] == "Colorado"]
# To get the specific value from row then column --> data[data.day == "Monday"].subject.item()
# TODO 4) Use loop to allow user to keep guessing
# TODO 5) Record the correct guesses in a list
# TODO 6) Keep track of the score
# To get cell in each row state_data = data[data.state == answer_state],  int(state_data.x), int(state_data.y)

screen.exitonclick()
