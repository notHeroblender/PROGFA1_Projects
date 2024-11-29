#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 21/11/2024

@author: pinke
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math
from pygame.math import Vector2

# to create enumerators, we need an extra import:
from enum import Enum

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(1000, 400)

# Set the frame rate to x frames per second:
engine.set_fps(60)


# enumerates all states the traffic light can be in:
class TrafficLight(Enum):
    GREEN = 0
    ORANGE = 1
    RED = 2
    BROKEN = 3


# variable to keep track of the traffic light state
#   this will be used each time to CHECK / CHANGE the traffic light state!
current_state = TrafficLight.GREEN


img_car = engine.load_image("Resources/car.png")
car_x = engine.width / 2
car_y = engine.height * 0.75

frame_count = 0


def draw_traffic_light():
    """
    Draws 3 lights underneath each other. If the light is off, it is gray.
    Otherwise, it has its own color (red,orange,green).
    To check if a light is on/off, we use the traffic light state (machine).
    In case of a broken traffic light, all lights will be off and a tick red line will appear over the traffic light.
    """
    x, y = 20, 20
    w, h = 40, 160
    distance = h / 6

    engine.shape_mode = ShapeMode.CENTER
    engine.outline_color = None
    gray = 0.3, 0.3, 0.3

    if current_state == TrafficLight.RED:       # change red light color based on current state
        engine.color = 1, 0, 0
    else:
        engine.color = gray
    engine.draw_circle(x + w/2, y + distance, w)

    if current_state == TrafficLight.ORANGE:    # change orange light color based on current state
        engine.color = 1, 1, 0
    else:
        engine.color = gray
    engine.draw_circle(x + w/2, y + distance * 3, w)

    if current_state == TrafficLight.GREEN:     # change green light color based on current state
        engine.color = 0, 1, 0
    else:
        engine.color = gray
    engine.draw_circle(x + w/2, y + distance * 5, w)

    if current_state == TrafficLight.BROKEN:    # draw red line if traffic light is BROKEN
        engine.outline_color = 0.8, 0, 0
        engine.draw_line(x, y, x+w, y+h, 4)


def draw_car():
    """
    Draws the car in its current position.
    """
    engine.shape_mode = ShapeMode.CORNER
    img_car.draw(car_x, car_y)


def move_car():
    """
    Moves the car towards the left until out of bounds, then respawns on the other side.
    If there's a green light, the car moves faster than if there's an orange light.
    When there's a red light - or the traffic light is broken - the car does not move.
    """
    global car_x
    if current_state == TrafficLight.GREEN:         # green light = fast move!
        car_x -= 10
    elif current_state == TrafficLight.ORANGE:      # orange light = slow down..
        car_x -= 4

    # reset on the other side
    if car_x + img_car.width < 0:
        car_x = engine.width


def next_traffic_light():
    """
    State transitions to the next traffic light state.
    green --> orange
    orange --> red
    red --> green
    """
    global current_state
    if current_state == TrafficLight.GREEN:     # green --> orange
        current_state = TrafficLight.ORANGE
    elif current_state == TrafficLight.ORANGE:  # orange --> red
        current_state = TrafficLight.RED
    elif current_state == TrafficLight.RED:     # red --> green
        current_state = TrafficLight.GREEN


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    engine.shape_mode = ShapeMode.CENTER
    engine.set_font_size(64)
    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.background_color = 0, 0, 0
    draw_traffic_light()
    draw_car()
    pass


def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    global frame_count
    frame_count += 1

    # automatic transition between traffic light states every 180 frames (3 seconds):
    if frame_count % 180 == 0:
        next_traffic_light()

    move_car()
    pass


def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    # click on window forces immediate traffic light state transition:
    next_traffic_light()
    pass


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    # transition between broken and not broken (green) state on each key press
    global current_state
    if not current_state == TrafficLight.BROKEN:    # not broken --> broken
        current_state = TrafficLight.BROKEN
    else:
        current_state = TrafficLight.GREEN          # broken --> not broken (green)
    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
