import turtle
import pandas

screen= turtle.Screen()
screen.title("US states games")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")

states = data["state"].to_list()

guess_states = []
while len(guess_states) < 50:
    answer = screen.textinput(title=f'Guessed {len(guess_states)}/50', prompt="Whats another state name?").title()

    if answer in states:
        guess_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

turtle.exitonclick()
#turtle.mainloop()

