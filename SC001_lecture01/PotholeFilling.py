"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:karel is (2,1)
    post-condition:karel is (2,7)
    """
    #Algorithm
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()


def go_in():
    """
    pre-condition:Karel is on the top of ground and facing east
    post-condition:Karel is underground and facing south
    """
    move()
    turn_right()
    move()

def go_out():
    """
    pre-condition:Karel is underground and facing south
    post-condition:Karel is on the top of ground and facing east
    """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()


def turn_right():
    for i in range(3):
        turn_left()


def put_99_beepers():
    for i in range(99):
        put_beeper()






def turn_right():
    for i in range(3):
        turn_left()

def put_99_beepers():
    for i in range(99):
        put_beeper()





# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
