#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 05/11/2024

@author: pinne
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


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    engine.background_color = 0,0,0

    pass


def draw_ghost(x: float, y: float, scale: float = 1.0, color: tuple[float, float, float] = (1, 1, 1)) -> None:

    # GIVEN:
    width = 90 * scale
    height = width * 1.5
    engine.shape_mode = ShapeMode.CORNER

    # TODO STUDENT: Code below should only be executed if left mouse button is pressed and mouse cursor hovers over the ghost
    # GIVEN:
    engine.color = color
    engine.outline_color = None

    engine.shape_mode = ShapeMode.CORNER
    engine.draw_arc(x, y, width, width, 180, 360)
    engine.draw_rectangle(x, y+width/2, width, height-width/2)

    eye_size = 28 * scale
    engine.color = 0, 0, 0
    engine.shape_mode = ShapeMode.CENTER
    distance = width/2.5
    engine.draw_circle(x + width/2 - distance/2, y+width/3, eye_size)
    engine.draw_circle(x + width/2 + distance/2, y+width/3, eye_size)

    mouth_size = eye_size * 1.3
    engine.draw_ellipse(x+width/2, y+width/1.4, mouth_size, mouth_size*1.2)

    # BOO
    engine.color = 1, 1, 1
    engine.draw_text("BOO!", x+width/2, y+height+10, centered=True)

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    draw_ghost(engine.width/4,engine.height/4*3,.5,(1,1,1))
    draw_ghost(engine.width/6*5,engine.height/2,1,(1,1,1))
    draw_ghost(engine.width/16*1,engine.height/8*1,1,(1,1,1))

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
    if mouse_button == MouseButton.LEFT:
        engine.background_color = 0,0,0
        print("Mouse left pressed at",mouse_x,mouse_y)
        engine.color = 1,1,0,.3
        engine.draw_circle(mouse_x, mouse_y, 200)

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
