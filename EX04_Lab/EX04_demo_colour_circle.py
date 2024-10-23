#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 18/10/2024

@author: Siska

/1. draw circle in the middle of the screen
/2. change colour circle based on the mouse pos
/3. change bg colour based on lmb or rmb
4. change bg random colour when pressing R
5. change circle outline based on if mouse is inside circle or not
"""
import random

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math

from pygame.examples.midi import key_class
from pygame.math import Vector2

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.set_fps(60)


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    draw_circle()
    pass

def draw_circle():
    """
    draws a circle that changes colour based on height of mouse
    :return:
    """
    engine.shape_mode = ShapeMode.CENTER #calculates shape pos from shape center

    if engine.mouse_y <= engine.height/3:
        engine.color = 1,0,0
    elif engine.mouse_y <= ((engine.height/3)*2):
        engine.color = 0,1,0
    else:
        engine.color = 0,0,1

    pos_x = engine.width*.5 #multiply is more efficient for pc than divide, so is ² over sqrt
    pos_y = engine.height*.5
    diameter = 200
    outline_width = 3

    if engine.colliding_point_in_circle(engine.mouse_x,engine.mouse_y,pos_x,pos_y,diameter):
        engine.outline_color = 1,1,1
    else:
        engine.outline_color = 0,1,1

    engine.draw_circle(pos_x,pos_y,diameter,outline_width)
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
    if mouse_button == mouse_button.LEFT:
        engine.background_color = 0,0,0
    if mouse_button == mouse_button.RIGHT:
        engine.background_color = 1,1,1
    if mouse_button == mouse_button.MIDDLE:
        engine.background_color = .5,.5,.5

    pass


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    r_key_pressed = (key == "r") | (key == "R") #brackets needed for |, not for or
    if r_key_pressed:
        engine.background_color = (random.uniform(0,1),
                                   random.uniform(0,1),
                                   random.uniform(0,1))
    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
