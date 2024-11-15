#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 15/11/2024

@author: pinne
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math
from pygame.math import Vector2

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(500, 500)

# Set the frame rate to x frames per second:
engine.set_fps(60)

size = 10

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    global size
    engine.outline_color = 0, 0, 0
    engine.shape_mode = ShapeMode.CENTER
    #diagonal \
    posx, posy = size*.5, size*.5
    while (posx <= engine.width) and (posy <= engine.height):
        engine.color = 0,0,1 #blue
        engine.draw_square(posx, posy, size)
        posx += size
        posy += size
    #diagonal /
    posx, posy = (engine.width - size * .5), size * .5
    while (posx >= 0) and (posy <= engine.height):
        engine.color = 1,1,0 #yellow
        engine.draw_square(posx, posy, size)
        posx -= size
        posy += size
    #top --
    posx, posy = size*.5, size*.5
    while posx <= engine.width:
        engine.color = 1, 0, 0  #red
        engine.draw_square(posx, posy, size)
        posx += size
    #bottom --
    posx, posy = size*.5, (engine.height - size * .5)
    while posx <= engine.width:
        engine.draw_square(posx, posy, size)
        posx += size
    #left |
    posx, posy = size * .5, size*.5
    while posy <= engine.height:
        engine.color = 0, 1, 0  # green
        engine.draw_square(posx, posy, size)
        posy += size
    #right |
    posx, posy = (engine.width - size * .5), size*.5
    while posy <= engine.height:
        engine.draw_square(posx, posy, size)
        posy += size
    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """

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
