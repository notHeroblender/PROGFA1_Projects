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

from dae_progfa_lib.progfa_image import ProgfaImage
from pygame.math import Vector2

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(960, 540)

# Set the frame rate to x frames per second:
engine.set_fps(60)


layers = []
layer_amt = 3

player_img:ProgfaImage

list_x_pos = []

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    global player_img

    for i in range(layer_amt):
        layers.append(engine.load_image(f"Resources/{i+1}.png"))
    #print(layers)

    player_img = engine.load_image("Resources/player.png")
    print(player_img)
    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    global player_img

    engine.background_color = (0.011764705882352941,0.1568627450980392,0.12549019607843137)

    for i in range(len(layers)):    #set every layer's x pos to 0
        list_x_pos.append(0)    #add one at 0
        list_x_pos.append(engine.width) #add one just off-screen

    for i in range(len(layers)):    #draw every layer
        layers[i].draw(list_x_pos[2*i],0)   #0,2,4...
        layers[i].draw(list_x_pos[2*i+1],0)   #1,3,5...

    animate_parallax(1)

    player_img.draw(0,0)

    pass

def animate_parallax(speed_multiplier):
    """
    animates the background with parallax effect
    :return:
    """
    global list_x_pos
    default_speed = 2
    offset = engine.width

    for i in range(0,len(list_x_pos),2):
        layer_nr = i//2 #0=0,1=0,2=1,3=1,4=2,5=2...

        speed = default_speed*(layer_nr+speed_multiplier)
        list_x_pos[i] -= speed
        list_x_pos[i+1] -= speed

        if list_x_pos[i] <= -offset:
            list_x_pos[i] += engine.width*2
        if list_x_pos[i+1] <= -offset:
            list_x_pos[i+1] += engine.width*2

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
