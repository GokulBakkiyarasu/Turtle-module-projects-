from turtle import Turtle, Screen
import random
race_on = False
screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter the color: ")
colors = ["red", "green", "yellow", "orange", "violet", "blue"]
all_turtle = []
x = -230
y = -100
z = 0
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[z])
    new_turtle.goto(x, y)
    all_turtle.append(new_turtle)
    z += 1
    y += 50
if user_bet:
    race_on = True
while race_on:
    for turtle in all_turtle:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won! The winning color is '{winning_color}'.")
            else:
                print(f"You lost. The winning color is '{winning_color}'.")
screen.exitonclick()


