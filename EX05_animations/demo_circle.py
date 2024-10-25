#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 25/10/2024

@author: pinne
"""

#/1. circle in the middle of the screen
#/2. move circle with random velocity
#/3. reset circle when outside screen
#/3.1.   detect if outside screen
#/3.2.   press "enter"
#/3.3.   put circle back in the middle
#/3.4.   new velo
#/4. click to change velocity/direction
#/5. text on top of circle
#?5.1.   typing adds, backspace deletes
#5.2.   if outside screen, change to FAIL
#6. fading trail behind circle

import random

from itertools import filterfalse
import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math

from pygame.draw import circle
from pygame.math import Vector2

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.set_fps(60)

# Global vars
circle_x = engine.width*.5
circle_y = engine.height*.5
circle_size = 200
circle_text = ""
vel_x = 0
vel_y = 0


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    engine.background_color = 1,1,1
    random_velocity()
    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    #engine.background_color = 1,1,1
    engine.shape_mode=ShapeMode.CORNER
    engine.color = 1,1,1,.1
    engine.outline_color = None
    engine.draw_rectangle(0,0,engine.width,engine.height)
    draw_text_circle(circle_x,circle_y,circle_size,circle_text)

    pass

def draw_text_circle(c_x:float,c_y:float, c_size:float,c_text:str=""):
    """
    draws circle with text in the middle
    :param c_x: circle x position
    :param c_y: circle y position
    :param c_size: circle size
    :param c_text: text displayed on circle
    :return:
    """
    engine.shape_mode = ShapeMode.CENTER
    engine.color = 1,0,0
    engine.outline_color = None

    engine.draw_circle(c_x,c_y,c_size)

    engine.color = 1,1,1
    engine.set_font_size(20)
    engine.draw_text(c_text,c_x,c_y,True)

def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    update_text_circle()

    pass

def update_text_circle():
    """
    moves circle with random velocity
    :return:
    """
    global circle_x, circle_y
    global vel_x,vel_y

    circle_x += vel_x
    circle_y += vel_y

def random_velocity():
    """
    assigns random velocity to variables between -3 and 3
    :return:
    """
    global vel_x, vel_y

    angle = random.uniform(0,360)
    math.radians(angle)

    speed = 5

    vel_x = math.cos(angle)*speed
    vel_y = math.sin(angle)*speed

def is_circle_in_rect(c_x:float,c_y:float,c_size:float,r_l:float,r_r:float,r_t:float,r_b:float)->bool:
    """
    :param c_x: center circle x
    :param c_y: center circle y
    :param c_size: circle size
    :param r_l: left side of rect
    :param r_r: right side of rect
    :param r_t: top of rect
    :param r_b: bot of rect
    :return: true if circle inside rectangle, false is=f not
    """
    if (c_x + c_size*.5 < r_l) | (c_x - c_size*.5 > r_r):
        return False
    if (c_y + c_size*.5 < r_t) | (c_y - c_size*.5 > r_b):
        return False

    return True

def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    """
    This function is only executed once each time a mouse button was pressed!
    """
    engine.shape_mode = ShapeMode.CENTER
    if ((mouse_button == mouse_button.LEFT) and
            (engine.colliding_point_in_circle(mouse_x,mouse_y,circle_x,circle_y,circle_size))):
        random_velocity()
    pass


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    global circle_x, circle_y, circle_size, circle_text
    if (key == "ENTER") and not (is_circle_in_rect(circle_x,circle_y,circle_size,
                         0,engine.width,0,engine.height)):
        circle_x = engine.width*.5
        circle_y = engine.height*.5
        random_velocity()
        circle_text = "Fail!"
    elif key.lower() in "qwertyuiopasdfghjklzxcvbnm!?., ":
        circle_text += key
    elif key == "BACKSPACE":
        #challenge: backspace one at a time
        circle_text = ""
    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
