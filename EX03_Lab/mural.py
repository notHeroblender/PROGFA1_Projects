#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 04/11/2024

@author: pinne
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math
from pygame.math import Vector2

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 800)

# Set the frame rate to x frames per second:
engine.set_fps(60)

black = (0.071, 0.071, 0.071)
white = (0.949, 0.949, 0.949)
red = (0.788, 0.114, 0.114)
green = (0.286, 0.71, 0.176)
blue = (0.176, 0.369, 0.71)
yellow = (0.871, 0.773, 0.082)
magenta = (0.78, 0.31, 0.667)
cyan = (0.251, 0.757, 0.812)

def diagonal_one(colour_top,colour_bot,posx,posy,size):
    """
    diagonal like this: ,-'
    :param colour_top:
    :param colour_bot:
    :param posx:
    :param posy:
    :param size:
    :return:
    """
    engine.color = colour_top
    engine.draw_triangle(posx,posy,posx+size,posy,posx,posy+size)

    engine.color = colour_bot
    engine.draw_triangle(posx+size,posy,posx+size,posy+size,posx,posy+size)
    pass

def diagonal_two(colour_top,colour_bot,posx,posy,size):
    """
    diagonal like this: '-,
    :param colour_top:
    :param colour_bot:
    :param posx:
    :param posy:
    :param size:
    :return:
    """
    engine.color = colour_top
    engine.draw_triangle(posx,posy,posx+size,posy,posx+size,posy+size)

    engine.color = colour_bot
    engine.draw_triangle(posx,posy,posx,posy+size,posx+size,posy+size)
    pass

def vertical_split(colour_left,colour_right,posx,posy,size):
    """
    split like this: |
    :param colour_left:
    :param colour_right:
    :param posx:
    :param posy:
    :param size:
    :return:
    """
    engine.color = colour_left
    engine.draw_rectangle(posx,posy,posx+(size/2),posy+size)

    engine.color = colour_right
    engine.draw_rectangle(posx+(size/2),posy,posx+size,posy+size)
    pass

def horizontal_split(colour_top,colour_bot,posx,posy,size):
    """
    split like this: --
    :param colour_top:
    :param colour_bot:
    :param posx:
    :param posy:
    :param size:
    :return:
    """
    engine.color = colour_top
    engine.draw_rectangle(posx,posy,posx+size,posy+(size/2))

    engine.color = colour_bot
    engine.draw_rectangle(posx,posy+(size/2),posx+size,posy+(size/2))
    pass

def circle_tile(colour_bg,colour_circle,posx,posy,size):
    """
    circle on a square
    :param colour_bg:
    :param colour_circle:
    :param posx:
    :param posy:
    :param size:
    :return:
    """
    engine.color = colour_bg
    engine.draw_square(posx,posy,size)

    engine.color = colour_circle
    engine.draw_circle(posx,posy,size)
    pass

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    engine.outline_color = None

    #mural one
    tile_size = engine.width/2

    diagonal_one(yellow,cyan,0,0,tile_size)
    diagonal_two(yellow,magenta,tile_size,0,tile_size)
    diagonal_two(magenta, yellow, 0, tile_size, tile_size)
    diagonal_one(cyan, yellow, tile_size, tile_size, tile_size)

    #mural two
    tile_size = engine.width/4
    #1
    vertical_split(red,white,0,0,tile_size)
    diagonal_two(blue,black,tile_size,0,tile_size)
    circle_tile(yellow,black,tile_size*2,0,tile_size)
    horizontal_split(red,white,tile_size*3,0,tile_size)
    #2
    diagonal_two(yellow,white,0,tile_size,tile_size)
    diagonal_one(black,red,tile_size,tile_size,tile_size)
    diagonal_two(white,black,tile_size*2,tile_size,tile_size)
    vertical_split(yellow,blue,tile_size*3,tile_size,tile_size)
    #3
    horizontal_split(black,white,0,tile_size*2,tile_size)
    diagonal_one(yellow,blue,tile_size,tile_size*2,tile_size)
    diagonal_two(black,blue,tile_size*2,tile_size*2,tile_size)
    circle_tile(red,white,tile_size*3,tile_size*2,tile_size)
    #4
    circle_tile(black,blue,0,tile_size*3,tile_size)
    diagonal_two(white,red,tile_size,tile_size*3,tile_size)
    diagonal_one(white,black,tile_size*2,tile_size*3,tile_size)
    horizontal_split(yellow,black,tile_size*3,tile_size*3,tile_size)

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
