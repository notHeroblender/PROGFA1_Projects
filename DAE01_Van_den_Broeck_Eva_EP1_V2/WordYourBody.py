#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 17/01/2025
WORK YOUR BODY V2
@author: Eva Van den Broeck, DAE01
"""
import random

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math

from dae_progfa_lib.progfa_image import ProgfaImage
from pygame.math import Vector2

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(600, 700)

# Set the frame rate to x frames per second:
engine.set_fps(60)

chosen_cals = 0
exercise_amt = 7
training_exercises = ['rope_skipping', 'spinning', 'arms', 'running', 'legs', 'lifting', 'moonwalking', 'abdominals']
exercises_to_do = []
exercise_imgs = []
imgs_to_do = []
training_calories = [180, 100, 50, 200, 50, 50, 120, 50]
cals_to_do = 0
training_minutes  = [10, 10, 10, 15, 10, 10, 15, 10]
minutes_to_do = 0


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    load_imgs()

    pass

def load_imgs():
    """
    loads all images from the resource/workyourbody folder and resizes them
    :return:
    """
    global exercise_imgs

    for i in range(exercise_amt):
        exercise_imgs.append(engine.load_image(f"Resources/WorkYourBody/{i + 1}_{training_exercises[i]}.jpg"))
    for img in exercise_imgs:
        img.resize(50,50,True)


    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.background_color = .9,.5,0
    draw_calorie_picker()
    draw_exercises()
    if len(exercises_to_do) != 0:
        draw_total()

    pass

def draw_calorie_picker():
    """
    draws the chosen calories on screen with instructions
    """
    engine.color = 1,1,1
    engine.set_font_size(18)
    engine.draw_text(f"How many CALORIES do you want to burn today? : {chosen_cals}", engine.width/2, 10, True)
    engine.set_font_size(14)
    engine.draw_text("(use UP and DOWN arrow keys to increase/decrease calories)", engine.width / 2, 10+30, True)

    pass

def draw_exercises():
    """
    draws the exercises with details and images under each other
    :return:
    """
    global imgs_to_do

    engine.set_font_size(14)
    for i in range(len(exercises_to_do)):
        engine.draw_text(f"{training_exercises[i]} - {str(training_minutes[i])} min",100,120+55*i)
        imgs_to_do[i].draw(engine.width/2, 100+55*i)
        engine.draw_text(f"{str(training_calories[i])} cals",engine.width/2+50, 120+55*i)

    pass

def draw_total():
    global minutes_to_do

    engine.set_font_size(14)
    engine.draw_text("Your exercises for today:", 20, 80)

    text_y = len(exercises_to_do)*55+120
    engine.set_font_size(18)
    engine.draw_text(f"GO FOR IT! Your training total will take {minutes_to_do} minutes today!", engine.width/2,text_y,True)
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
    update_cals(key)
    if key.lower() == "r":
        reset_cals()
    if key.lower() == "x":
        random_cals()

    pass

def reset_cals():
    global chosen_cals
    chosen_cals = 0
    calculate_exercises()

def random_cals():
    global chosen_cals
    chosen_cals = random.randrange(0,800,100)
    calculate_exercises()

def update_cals(k):
    """
    updates the chosen calories by in-/decreasing the value by 100
    :param k: key pressed
    """
    global chosen_cals
    if   k == "UP" and chosen_cals < 800:
        chosen_cals += 100
        if chosen_cals > 800:
            chosen_cals = 800
    elif k == "DOWN" and chosen_cals > 0:
        chosen_cals -= 100
        if chosen_cals < 0:
            chosen_cals = 0

    calculate_exercises()
    pass

def calculate_exercises():
    global exercises_to_do, cals_to_do, minutes_to_do

    cals_to_do = 0
    minutes_to_do = 0
    exercises_to_do.clear()
    imgs_to_do.clear()
    for i in range(len(training_exercises)):
        if chosen_cals > cals_to_do:
            cals_to_do += training_calories[i]
            minutes_to_do += training_minutes[i]
            exercises_to_do.append(training_exercises[i])
            imgs_to_do.append(exercise_imgs[i])
            print(f"{len(imgs_to_do)} images to do")

# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
