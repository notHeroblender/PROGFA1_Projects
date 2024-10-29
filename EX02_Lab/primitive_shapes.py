#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 24/10/2024

@author: pinne
"""
from shutil import which

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
    engine.background_color = 1, 1, 1
    pass

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    draw_shape_4()

    pass

def draw_shape_1():
    """
    draws two arrows pointing down
    :return:
    """
    engine.shape_mode = ShapeMode.CENTER
    engine.background_color = 1, 1, 1
    engine.color = 0, 0, 0
    engine.outline_color = 0, 0, 0

    engine.draw_triangle(0, 0,
                         engine.width, 0,
                         engine.width / 2, engine.height / 2, 0)
    engine.draw_triangle(0, engine.height / 2,
                         engine.width, engine.height / 2,
                         engine.width / 2, engine.height, 0)
    pass

def draw_shape_4():
    """
    draws 4 black circles and a white square in the middle of them
    :return:
    """
    engine.shape_mode = ShapeMode.CENTER
    engine.color = 0, 0, 0
    engine.outline_color = None

    #                     middle x         middle y        diameter
    engine.draw_ellipse(engine.width/4, engine.height/4, engine.width/2, engine.height/2,)
    engine.draw_ellipse(engine.width/4*3, engine.height/4, engine.width/2, engine.height/2)
    engine.draw_ellipse(engine.width/4, engine.height/4*3, engine.width/2, engine.height/2)
    engine.draw_ellipse(engine.width/4*3, engine.height/4*3, engine.width/2, engine.height/2)

    engine.color = 1,1,1
    engine.draw_rectangle(engine.width*.5,engine.height*.5,engine.width*.5,engine.height*.5)
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
