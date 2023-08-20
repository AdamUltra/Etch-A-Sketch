from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def move_down():
    tim.right(10)


def move_up():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(move_forwards, 'w')
screen.onkeypress(move_backwards, 's')
screen.onkeypress(move_down, 'd')
screen.onkeypress(move_up, 'a')
screen.onkeypress(clear, 'c')
screen.exitonclick()

