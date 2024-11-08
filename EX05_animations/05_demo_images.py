#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 08/11/2024

@author: pinne
"""

#/ 1. set font
#/ 2. draw text
# 3. add text
# 4. backspace delete
# 5. load image
# 6. draw image
# 7. stretch goals

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math
from pygame.math import Vector2

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.set_fps(60)

text = "Kachow!"
img = engine.load_image("RetroComic.png")

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    global img

    engine.set_font("CrashLandingBB.ttf")
    engine.shape_mode = ShapeMode.CENTER
    engine.set_font_size(200)
    print(img)

    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    global img
    img.draw_fixed_size(engine.width*.5,engine.height*.5,engine.width,engine.height,False)

    engine.color = 0, 0, 0
    engine.draw_text(text, engine.width / 2 + 10, engine.height / 2 + 10, True)
    engine.color = 1,.4,.1
    engine.draw_text(text, engine.width / 2, engine.height / 2, True)

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
    global text
    allowed = "!","?",".",","," "

    if key == "BACKSPACE":
        text = ""
    elif key.isalpha() and len(key)==1 or (key in allowed): #disallow ctrl, enter, etc
        text += key

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
