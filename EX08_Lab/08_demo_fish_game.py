#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 29/11/2024

@author: pinne
"""
import random

"""
1. Fish
/    a. vars: xpos, ypos, speed, left img, right img
/    b. load images, init fish vars
/        - start left outside of screen -> 0-size
/        - starts with pos speed (moving right)
/        - resize fish to 100x100
/    c. draw one fish
/        - pick which image based on speed (neg=L,pos=R)
/    d. update fish
/        - always moving: xpos += speed
/        - if outside, flip fish
/            - new ypos, other fish frame
2. Bubbles (start with one)
/    a. vars: 
/        - list xpos[xpos,xpos,xpos], list ypos[ypos,ypos,ypos] || list of list of xypos[[xpos,ypos],[xpos,ypos]], 
/        - size = 20
/        - max amt = 5
        - opt vars: bub_min_x_speed, bub_max_x_speed, bub_min_y_speed, bub_max_y_speed
-    b. opt: init bubbles -> clear lists, to start over
/    c. spawn bubble
/        - if amt < max amt, add bubble to list at mousepos
/    d. draw bubble
/        - draw circle for each var in list
    e. update bubble
        - always moving, rand x speed (-2,2), rand y speed (.1,2)
            - opt: keep inside x=0 and x=width
        - if off screen, remove from list (hint in doc)
            - -5 score
        - if collide fish, remove from list (hint in doc)
            - +1 score
        !!! remove back to front, not front to back in list
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

from random import randint
from dae_progfa_lib.progfa_image import ProgfaImage

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(600, 800)

# Set the frame rate to x frames per second:
engine.set_fps(60)

#fish vars
fish_l_r = []
f_x_pos = 0
f_y_pos = 0
f_speed = 0
#temp
fish_l:ProgfaImage
fish_r:ProgfaImage
#bubble vars
b_pos = []
b_max = 0
b_size = 0

#ui vars

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    init_fish()
    init_bubbles()
    pass

def init_fish():
    global fish_l_r, fish_l, fish_r, f_x_pos, f_y_pos, f_speed

    fish_l = engine.load_image("Resources/fish_L.png")
    fish_r = engine.load_image("Resources/fish_R.png")

    fish_l.resize(100,100,True)
    fish_r.resize(100,100,True)

    fish_l_r.append(fish_l)
    fish_l_r.append(fish_r)

    f_x_pos = 110
    f_y_pos = 200

    f_speed = 5
    pass
def init_bubbles():
    global b_max, b_size, b_pos

    b_pos = []
    b_max = 5
    b_size = 30

    temp_pos = [engine.width/2, engine.height/2]
    b_pos.append(temp_pos)
    pass

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.background_color = 0.216, 0.502, 0.812
    draw_fish()
    draw_bubbles()
    pass

def draw_fish():
    """
    draws a fish using the global f_x_pos, f_y_pos. left or right facing is calculated using f_speed
    :return:
    """
    global f_x_pos,f_y_pos, f_speed

    if (f_x_pos < -100) | (f_x_pos>engine.width):
        f_y_pos = randint(0,engine.height)
        f_speed *= -1

    if f_speed < 0:
        fish_l_r[0].draw(f_x_pos, f_y_pos)
    else:
        fish_l_r[1].draw(f_x_pos,f_y_pos)
    pass

def draw_bubbles():
    global b_max, b_size, b_pos

    engine.outline_color = 1,1,1
    engine.color = 0,0,0,0

    for pos in b_pos:
        engine.draw_circle(pos[0], pos[1],b_size,2)
    pass


def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    update_fish()
    update_bubbles()
    pass

def update_fish():
    global f_x_pos, f_y_pos, f_speed

    f_x_pos += f_speed
    pass

def update_bubbles():
    global b_max, b_size, b_pos
    #- always moving, rand x speed (-2,2), rand y speed (.1,2)
    for pos in b_pos:
        pos[0] += randint(-2,2)
        pos[1] -= random.uniform(.1,2)

    pass


def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    """
    This function is only executed once each time a mouse button was pressed!
    """
    global b_max, b_pos

    if len(b_pos) < b_max:
        b_pos.append([mouse_x, mouse_y])

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
