"""
Defines functionality for the turtle assignment
"""

import turtle
from time import sleep

# Stores ASCII keycodes
keys = []

# Callback for Turtle input
def keypress(e):
    keys.append(e.char)

# Create turtle context
t = turtle.Turtle()
s = turtle.Screen()
s._root.bind("<KeyPress>", keypress)

# Move the pen forward
def forward(n):
    t.forward(n * 10)

# Turn the pen
def turn(n):
    t._rotate(n * -1)

# Change the ink color
def change_color_to(color):
    t.pencolor(color)

# Get input ASCII keycodes
def get():
    while len(keys) == 0:
        try:
            s._root.update()
            if len(keys) > 0:
                # Remove keys if their code is empty
                for key in keys:
                    if not key:
                        keys.remove(key)
        except:
            raise SystemExit
        sleep(0.1)
    
    c = ord(keys.pop(0))
    return c
    
# Run the program
def run(program):
    while True:
        program()
