#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 22/11/2024

@author: pinne
"""

#/1. draw star
#/2. give random pos to star
#/3. move star to left
#/4. if reaches left, move to the other side of the screen
#5. more stars

import random
import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.set_fps(60)

x_pos = 0
y_pos = 0
list_x_pos = []
list_y_pos = []
start_star_amount = 15

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    random_position()

    pass

def draw_star(x:int,y:int)->None: #-> (x: int | float) -> x can be int or float
    """
    draws a star on x,y with the size of 2 pixels
    :param x: center x pos
    :param y: center y pos
    :return: None
    """
    engine.shape_mode = ShapeMode.CENTER
    engine.outline_color = None
    engine.color = 1,1,1,0.8
    size = 2
    engine. draw_circle(x,y,size)

def random_position():
    """
    generates a random value for the global x_pos and y_pos
    :return:
    """
    global x_pos, y_pos
    #x_pos = (random.randint(0, engine.width)) # single star
    #y_pos = (random.randint(0, engine.height)) # single star

    for i in range(start_star_amount):
        list_x_pos.append(random.randint(0, engine.width))
        list_y_pos.append(random.randint(0, engine.height))

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.background_color = 0,0,0.1
    #draw_star(x_pos,y_pos) # single star
    for i in range(start_star_amount):
        draw_star(list_x_pos[i],list_y_pos[i])

    pass

def move(speed:int = 2):
    """
    moves object
    :param speed: how fast it moves, positive = moving left, negative = moving right
    :return:
    """
    global x_pos
    global list_x_pos
    speed = 2
    offset = 3
    #x_pos -= speed # single star
    #if x_pos <= -offset: # single star
    #    x_pos += engine.width + (offset*2) #offset = small visual buffer # single star
    for i in range(start_star_amount):
        list_x_pos[i] -= speed
        if list_x_pos[i] <= -offset:
            list_x_pos[i] += engine.width + (offset * 2)  # offset = small visual buffer

def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    move()

    pass


def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    """
    This function is only executed once each time a mouse button was pressed!
    """
    global start_star_amount
    if mouse_button == MouseButton.LEFT:
        list_x_pos.append(random.randint(0, engine.width)) # single star
        list_y_pos.append(random.randint(0, engine.height)) # single star
        start_star_amount += 1

    pass


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    global start_star_amount
    if start_star_amount > 0:
        list_x_pos.pop()
        list_y_pos.pop()
        start_star_amount -= 1
    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
