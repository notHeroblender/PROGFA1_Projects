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
from enum import Enum
import random

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(960, 540)

# Set the frame rate to x frames per second:
engine.set_fps(60)

#UI
bg_img:ProgfaImage
btn_img:ProgfaImage
score = 0
mistakes = 0
btn_offset = 0
btn_width = 0
btn_height = 0
start_btn_x = 0
start_btn_y = 0
quit_btn_x = 0
quit_btn_y = 0

#GAMEPLAY
#Visuals
layers = []
layer_amt = 5
player_img:ProgfaImage
player_sprite_width = 0
ground_height = engine.height - 160
list_x_pos = []
#Logic
typed_letters = ""
displayed_word = ""
current_words = []
easy_words = ["cat", "dog", "book", "tree", "star", "fish", "blue", "apple", "chair", "house", "train",
              "light", "happy", "mouse", "plane", "smile", "paper", "cloud", "water", "horse"]
medium_words = []
hard_words = []

class GameState(Enum):
    START = 0
    PLAY = 1
    END = 2

current_state = GameState.START

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    init_start()
    init_gameplay()
    init_end()

    pass

def init_start():
    global bg_img, btn_img,  btn_offset, btn_width, btn_height,\
        start_btn_x, start_btn_y,\
        quit_btn_x, quit_btn_y

    bg_img = engine.load_image("Resources/UI/bg.png")
    btn_img = engine.load_image("Resources/UI/btn.png")

    bg_img.resize(engine.width,engine.height,False)
    btn_img.resize(250,75,False)

    start_btn_x = engine.width / 2 - (btn_img.width / 2)
    start_btn_y = engine.height / 2 - (btn_img.height / 2)

    quit_btn_x = engine.width / 2 - (btn_img.width / 2)
    quit_btn_y = engine.height / 2 + btn_img.height / 2 + btn_offset

    btn_offset = 10
    btn_width = btn_img.width
    btn_height = btn_img.height

    pass

def init_end():
    pass

def init_gameplay():
    """
    puts the right values in the global variables needed for the gameplay
    :return:
    """
    global player_img, current_words, player_img, layers, player_sprite_width

    for i in range(layer_amt):
        layers.append(engine.load_image(f"Resources/{i + 1}.png"))
    for j in range(len(layers)):
        layers[j].resize(engine.width,engine.height,False)

    player_img = engine.load_image("Resources/Run.png")
    player_img.resize(1350, 200,True)
    player_sprite_width = player_img.width/9

    #set difficulty
    current_words.clear()
    current_words.extend(easy_words)

    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    if current_state == GameState.START:
        draw_start()
    if current_state == GameState.PLAY:
        draw_visuals()
        draw_game_text()

    pass

def draw_start():
    """
    draws the start menu background image with two buttons in the middle, one to start the game and one to quit the program
    :return:
    """
    engine.color = 1,1,1
    engine.set_font_size(34)

    bg_img.draw(0,0)

    btn_img.draw(start_btn_x, start_btn_y)
    engine.draw_text("START GAME", engine.width/2, engine.height/2, True)
    btn_img.draw(quit_btn_x, quit_btn_y+btn_offset)
    engine.draw_text("QUIT", engine.width/2,engine.height/2+btn_height+btn_offset, True)
    
    pass

def draw_visuals():
    """
    draws the visuals (background and player)
    :return:
    """
    global player_img, player_sprite_width

    engine.background_color = (0.5607843137254902, 0.8235294117647058, 0.2980392156862745)

    for i in range(len(layers)):  # set every layer's x pos to 0
        list_x_pos.append(0)  # add one at 0
        list_x_pos.append(engine.width)  # add one just off-screen

    for i in range(len(layers)):  # draw every layer
        layers[i].draw(list_x_pos[2 * i], 0)  # 0,2,4...
        layers[i].draw(list_x_pos[2 * i + 1], 0)  # 1,3,5...

    animate_parallax(1)

    player_img.draw_partial(60,ground_height,(0,0,player_img.height,player_sprite_width))

    pass

def draw_game_text():
    """
    draws words on the screen and colours them as you type
    :return:
    """
    global current_words,displayed_word,typed_letters

    engine.set_font_size(20)
    engine.color = 1,1,1
    engine.draw_text(displayed_word, engine.width/2,engine.height/2)

    #draws green regardless if correct or not
    engine.color = 0,1,0
    engine.draw_text(typed_letters, engine.width/2,engine.height/2)

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
    global current_state
    if current_state == GameState.START:
        if (start_btn_x < mouse_x < start_btn_x+btn_width) and (start_btn_y < mouse_y < start_btn_y+btn_height) :
            current_state = GameState.PLAY
            next_word() #display starter word
        elif (quit_btn_x < mouse_x < quit_btn_x+btn_width) and (quit_btn_y+btn_offset < mouse_y < quit_btn_y+btn_height+btn_offset):
            quit()

    pass


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    if current_state == GameState.PLAY:
        if key.isalpha():
            spell_checker(key)
        elif key == " ":
            next_word()

    print(f"score: {score}, mistakes: {mistakes}")

    pass

def spell_checker(k):
    """
    checks if the typed letter is the same as the next letter in the displayed word.
    :param k: pressed key
    :return:
    """
    global current_words, displayed_word, typed_letters, mistakes
    if k == displayed_word[len(typed_letters)]:
        print(f"{k.lower()} - 👍 (Green)")
        typed_letters += k
        if displayed_word == typed_letters: #if word complete
            next_word()
    else:
        print(f"{k.lower()} - wrong, new word (Red)")
        displayed_word = random.choice(current_words)
        typed_letters = ""
        mistakes += 1

    pass

def next_word():
    """
    picks what to do when a new word is picked
    :return:
    """
    global current_words, displayed_word, typed_letters, score, mistakes

    if typed_letters == displayed_word:
        print(f"{typed_letters} - is correct (Yellow)")
        typed_letters = ""
        score += 1
    else:
        print(f"{typed_letters} - wrong spelling (Red)")
        typed_letters = ""
        mistakes += 1
    displayed_word = random.choice(current_words)

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
