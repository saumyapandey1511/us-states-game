import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_state=[]
TOTAL_STATES = 50

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)


while len(guessed_state) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_state)}/{TOTAL_STATES} States Correct", prompt="whats another state name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_state]
        states_to_learn_csv = pandas.DataFrame(missing_states)
        states_to_learn_csv.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = data[data.state == answer_state]
        new_turtle.goto(int(state_data.x),int(state_data.y))
        new_turtle.write(state_data.state.item())
        new_turtle.write(answer_state)

