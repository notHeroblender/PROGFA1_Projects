#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 22/11/2024

@author: pinne
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math

from dae_progfa_lib.progfa_image import ProgfaImage
from pygame.math import Vector2

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(300, 300)

# Set the frame rate to x frames per second:
engine.set_fps(60)

frames = []
frames_amt = 4

current_frame = 1
timer = 0
max_timer = 10

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    for i in range(frames_amt):
        frames.append(engine.load_image(f"Resources/crewmates/green{i+1}.png"))
    print(frames)

    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    global current_frame
    engine.background_color = 1,1,1

    draw_frame(current_frame)

    pass

def draw_frame(frame:int=0):
    """
    draw a crewmate image based on frame
    :param frame:
    :return:
    """
    img:ProgfaImage = frames[frame] #long way to see the functions instead of frames[frame].draw()
    img.draw(0,0)

    #Debug
    engine.set_font_size(20)
    engine.color = 0,0,0
    engine.draw_text(str(frame),20,20)

    pass


def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    global current_frame, timer
    timer += 1
    if timer >= max_timer:
        timer = 0
        current_frame += 1
        # Logic
        #if current_frame >= len(frames):
        #    current_frame = 0
        # Math
        current_frame %= len(frames) # % remainder after div in full nr -> 0,1,2,3,0,1,2,3, etc

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
