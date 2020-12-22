import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()
correct_ans = []

while len(correct_ans) < 50:
    answer_state = screen.textinput(title=f"{len(correct_ans)}/50 States Correct",
                                    prompt="What's another state's name: ").title()
    if answer_state == "Exit":
        to_learn = []
        for i in states_list:
            if i not in correct_ans:
                to_learn.append(i)
        data = pandas.DataFrame(to_learn)
        data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list and answer_state not in correct_ans:
        correct_ans.append(answer_state)
        new = turtle.Turtle()
        new.hideturtle()
        new.penup()
        x = int(states[states.state == answer_state].x)
        y = int(states[states.state == answer_state].y)
        new.goto(x, y)
        new.write(answer_state, align='center')
