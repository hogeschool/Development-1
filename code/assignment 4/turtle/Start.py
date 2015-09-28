import turtle
from turtle import Vec2D


t = turtle.Turtle()


def down():
    t._orient = Vec2D(1.0, 1.0)


def forward(n):
    t.forward(n * 10)


class Direction:
    Up = 1
    Down = 2
    Left = 3
    Right = 4


class Color:
    Red = "red"
    Blue = "blue"
    Black = "black"
    Green = "green"

Red = Color.Red
Blue = Color.Blue
Black = Color.Black
Green = Color.Green


def change_color_to(color):
    t.pencolor(color)


def turn(n):
    if not (type(n) is Direction.Up):
        t._rotate(n * -1)
    else:
        if n == Direction.Up:
            t._orient = Vec2D(0, 1.0)
        if n == Direction.Left:
            t._orient = Vec2D(-1.0, 0)
        if n == Direction.Down:
            t._orient = Vec2D(0, -1.0)
        if n == Direction.Right:
            t._orient = Vec2D(1.0, 0)


def get():
    from msvcrt import getch
    c = ord(getch())
    ## On a Mac or Unix, you can uncomment the lines below
    ## and comment the two lines above.
    #import termios, sys, os
    #TERMIOS = termios
    #fd = sys.stdin.fileno()
    #old = termios.tcgetattr(fd)
    #new = termios.tcgetattr(fd)
    #new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    #new[6][TERMIOS.VMIN] = 1
    #new[6][TERMIOS.VTIME] = 0
    #termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    #c = None
    #try:
    #    c = ord(os.read(fd, 1))
    #finally:
    #    termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c


def run(a):
    while True:
        a()
