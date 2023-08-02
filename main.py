from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle_bg = Turtle()
turtle_txt = Turtle()
turtle_txt.hideturtle()
screen.title('U.S State Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle_bg.shape(image)

game_on = True
correct = 0

guessed_states = []
data = pandas.read_csv('50_states.csv')

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{correct}/50 Guess A State", prompt="Guess a state fool!").title()
    if answer == 'Exit':
        break
    for state in data.state:
        if answer == state and answer not in guessed_states:
            guessed_states.append(answer)
            correct += 1
            answer_info = data[data.state == answer]
            x_coor = int(answer_info.x)
            y_coor = int(answer_info.y)
            turtle_txt.penup()
            turtle_txt.goto(x_coor, y_coor)
            turtle_txt.write(arg=answer)


states_to_learn = [state for state in data.state if state not in guessed_states]
# for state in data.state:
#     if state not in guessed_states:
#         states_to_learn.append(state)

learn_dict = {
    'remaining states': states_to_learn,
}

learn_states = pandas.DataFrame(learn_dict)
learn_states.to_csv('States to learn')
