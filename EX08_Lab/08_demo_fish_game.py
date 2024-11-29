#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 29/11/2024

@author: pinne
"""

"""
1. Fish
    a. vars: xpos, ypos, speed, left img, right img
    b. load images, init fish vars
        - start left outside of screen -> 0-size
        - starts with pos speed (moving right)
        - resize fish to 100x100
    c. draw one fish
        - pick which image based on speed (neg=L,pos=R)
    d. update fish
        - always moving: xpos += speed
        - if outside, flip fish
            - new ypos, other fish frame
2. Bubbles (start with one)
    a. vars: 
        - list xpos[xpos,xpos,xpos], list ypos[ypos,ypos,ypos] || list of list of xypos[[xpos,ypos],[xpos,ypos]], 
        - size = 20
        - max amt = 5
        - opt vars: bub_min_x_speed, bub_max_x_speed, bub_min_y_speed, bub_max_y_speed
    b. opt: init bubbles -> clear lists, to start over
    c. spawn bubble
        - if amt < max amt, add bubble to list at mousepos
    d. draw bubble
        - draw circle for each var in list
    e. update bubble
        - always moving, rand x speed (-2,2), rand y speed (.1,2)
            - opt: keep inside x=0 and x=width
        - if off screen, remove from list (hint in doc)
            - -5 score
        - if collide fish, remove from list (hint in doc)
            - +1 score
3. UI
    a. vars: score
    b. draw score
    c. draw ammo (0 bub = 5 ammo)
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math
from pygame.math import Vector2

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.set_fps(60)

#fish vars
fish_l_r = []
#bubble vars
#ui vars

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

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
