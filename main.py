import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


''' HOW TO GET X,Y COOR BY CLICK:------------------
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop() # CODE WILL RUN IN LOOP--OPPOSITE OF exitonclick()
'''

score = 0
answer_list = []


data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()


while score < 50:
    answer_input = screen.textinput(
        title=f"{score}/50", prompt="Enter the name of a state").title()

    if answer_input == "Exit":
        missing_states = [state for state in states_list if state not in answer_list]
        break

    elif answer_input in answer_list:
        score += 0

    else:
        if answer_input in states_list:
            answer_list.append(answer_input)
            t = turtle.Turtle()
            score += 1
            state_data = data[data.state == answer_input]
            t.ht()
            t.pu()
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_input)


# statestolearn.csv
for data[data.state[0]] in not answer_list:
    list.append(data[data.state[0]])
    data = pandas.DataFrame(list)
    data.to_csv("States_to_learn.csv")
