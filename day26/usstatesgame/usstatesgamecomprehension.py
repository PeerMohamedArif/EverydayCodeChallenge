import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("US States Guess Game")
image="blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
guessed_states=[]
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop()# to keep the window open for multiple clicks
while len(guessed_states)<50:

    answer_state=screen.textinput(title=f" {len(guessed_states)}/50 States correct ",
                                  prompt="What is another state name?").title()
    data=pd.read_csv("50_states.csv")
    all_states=data.state.to_list()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        #print("saved")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        coordinates=data[data["state"]==answer_state]
        t.goto(int(coordinates["x"].item()),int(coordinates["y"].item())) # item is used to gets the first element alone
        t.write(answer_state)

screen.exitonclick()


