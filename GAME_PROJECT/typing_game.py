#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 26/11/2024

@author: pinne
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math
from pygame.math import Vector2

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(960, 540)

# Set the frame rate to x frames per second:
engine.set_fps(60)

layers = []
layer_amt = 4

list_x_pos = []

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    for i in range(layer_amt):
        layers.append(engine.load_image(f"Resources/{i+1}.png"))
    print(layers)
    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """

    engine.background_color = (0.011764705882352941,0.1568627450980392,0.12549019607843137)

    layers[0].draw(0,0)
    layers[1].draw(0,0)
    layers[2].draw(0,0) #player
    layers[3].draw(0,0)

    pass

def animate_parallax(layer:int):
    """
    animates the background with parallax effect
    :return:
    """
    global list_x_pos
    speed = 2
    offset = 3
    # x_pos -= speed # single star
    # if x_pos <= -offset: # single star
    #    x_pos += engine.width + (offset*2) #offset = small visual buffer # single star
    for i in range(len(list_x_pos)):  # do not use start amount, list has length
        list_x_pos[i] -= speed
        if list_x_pos[i] <= -offset:
            list_x_pos[i] += engine.width + (offset * 2)  # offset = small visual buffer
    pass


def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """

    pass


def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    """
    This function is only executed once each time a mouse button was pressed!
    """

    pass


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
