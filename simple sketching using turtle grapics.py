from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def move_clockwise():
    tim.right(10)


def move_counterclockwise():
    tim.left(10)


def reset():
    tim.clear()
    tim.reset()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_clockwise, "d")
screen.onkey(move_counterclockwise, "a")
screen.onkey(reset, "c")
screen.exitonclick()
