import pandas
import turtle

screen = turtle.Screen()
screen.setup(700, 700)
screen.title("India States Game")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("india_states.txt")

all_states_of_india = data.state.to_list()

guessed_states = []
while len(guessed_states) < 28:
    user_answer = screen.textinput(title= f"{len(guessed_states)}/28 States Guessed Correctly", prompt= "Guess a state?").title()

    if user_answer in all_states_of_india and user_answer not in guessed_states:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == user_answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(user_answer)

    if user_answer == "Exit":
        missing_states = []
        for state in all_states_of_india:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        df = pandas.DataFrame(missing_states)
        df.to_csv("States_to_learn.csv")
        break









