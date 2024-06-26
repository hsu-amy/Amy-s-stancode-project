"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    pre-condition:karel is on the wall's left side and facing east
    post-condition:Karel is on the wall's right side and facing south
    :return:
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition:Karel is on the wall's left, facing east
    post-condition:Karel is on the wall's top, facing east
    """
    turn_left()
    while not right_is_clear():
        move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()


def cross():
    move()
    turn_right()


def down():
    while front_is_clear():
        move()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
