import turtle as t
import random

is_race_on = False
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']



screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet", prompt="Enter a color (red/orange/yellow/green/blue/purple):")


y_positions = [-75, -45, -15, 15, 45, 75]
turtle_list = []
for turtle_index in range(len(colors)):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-240, y_positions[turtle_index])
    turtle_list.append(new_turtle)
# Draw the finish line
line = t.Turtle()
line.hideturtle()
line.penup()
line.goto(230, -150)
line.pendown()
line.goto(230, 150)

if user_bet:
    is_race_on = True

winner = ''
while is_race_on:
    for turtle in turtle_list:
        rand_num = random.randint(0, 5)
        turtle.forward(rand_num)
        if turtle.xcor() >= 212:
            winner = turtle.pencolor()
            is_race_on = False
            break
    if winner:
        if winner == user_bet:
            print(f"You win. The winner is the {winner.upper()} turtle!")
        else:
            print(f"{user_bet.upper()} lose. The winner is the {winner.upper()} turtle!")

screen.exitonclick()
