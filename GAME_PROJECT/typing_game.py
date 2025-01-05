#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 26/11/2024

@author: pinne
"""
from email.policy import default

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
diff_btn_img:ProgfaImage
score = 0
mistakes = 0
btn_offset = 0
btn_width = 0
btn_height = 0
start_btn_x = 0
start_btn_y = 0
quit_btn_x = 0
quit_btn_y = 0
diff_btn_width = 0
diff_btn_y = 0
easy_btn_x = 0
medium_btn_x = 0
hard_btn_x = 0

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
displayed_words = []
max_word_amt = 0
focused_word_idx = 0
current_words = []
easy_words = [
    "cat", "dog", "book", "tree", "star", "fish", "blue", "apple", "chair", "house", "train",
    "light", "happy", "mouse", "plane", "smile", "paper", "cloud", "water", "horse", "cup",
    "ball", "green", "jump", "table", "dance", "piano", "rain", "door", "car", "bread", "baby",
    "bird", "snow", "school", "clock", "phone", "bed", "shoe", "cake"]
medium_words = [
    "pencil", "window", "flower", "garden", "silver", "bridge", "laptop", "orange", "pirate", "rocket",
    "castle", "jungle", "planet", "wizard", "saddle", "sunset", "shadow", "forest", "basket", "thunder",
    "helmet", "camera", "mirror", "statue", "breeze", "lantern", "tunnel", "village", "eagle", "whisper",
    "luggage", "trophy", "dragon", "stream", "compass", "parrot", "crystal", "guitar", "harvest", "island"]
hard_words = [
    "quizzical", "xylophone", "jubilant", "subtlety", "chrysanthemum", "encyclopedia", "ambiguity",
    "juxtapose", "vortex", "zeppelin", "facetious", "haphazard", "syzygy", "phosphorescent", "labyrinthine",
    "dichotomy", "ephemeral", "persnickety", "onomatopoeia", "fluorescent", "ineffable", "obfuscate",
    "proclivity", "mellifluous", "antediluvian", "preposterous", "conundrum", "effervescent", "serendipity",
    "transcendent", "cacophony", "apocryphal", "ethereal", "sanguine", "idiosyncrasy", "zeitgeist", "epiphany",
    "nefarious", "lugubrious", "iridescent"]

speed = 0
default_speed = 0
speed_incr = 0
speed_decr = 0
speed_time = 0
speed_timer = 0

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
    global bg_img, btn_img, diff_btn_img, btn_offset, btn_width, btn_height,\
        start_btn_x, start_btn_y, quit_btn_x, quit_btn_y,\
        diff_btn_width, diff_btn_y, easy_btn_x,medium_btn_x,hard_btn_x

    bg_img = engine.load_image("Resources/UI/bg.png")
    btn_img = engine.load_image("Resources/UI/btn.png")
    diff_btn_img = engine.load_image("Resources/UI/btn.png")

    bg_img.resize(engine.width,engine.height,False)
    btn_img.resize(250,75,False)
    diff_btn_img.resize(250*2/3,75,False)

    quit_btn_x = engine.width / 2 - (btn_img.width / 2)
    quit_btn_y = engine.height / 2 + btn_img.height / 2 + btn_offset

    btn_offset = 10
    btn_width = btn_img.width
    btn_height = btn_img.height
    diff_btn_width = btn_img.width*2/3
    diff_btn_y = engine.height / 2 - (btn_img.height / 2)
    easy_btn_x = engine.width / 2 - (diff_btn_img.width / 2) - diff_btn_width - btn_offset
    medium_btn_x = engine.width / 2 - (diff_btn_img.width / 2)
    hard_btn_x = engine.width / 2 - (diff_btn_img.width / 2) + diff_btn_width + btn_offset

    pass

def init_end():
    #TODO: draw end screen
    pass

def init_gameplay():
    """
    puts the right values in the global variables needed for the gameplay
    :return:
    """
    global player_img, layers, player_sprite_width, current_words, max_word_amt, focused_word_idx, \
        speed, default_speed, speed_incr, speed_decr, speed_time, speed_timer

    for i in range(layer_amt):
        layers.append(engine.load_image(f"Resources/{i + 1}.png"))
    for j in range(len(layers)):
        layers[j].resize(engine.width,engine.height,False)

    player_img = engine.load_image("Resources/Run.png")
    player_img.resize(1350, 200,True)
    player_sprite_width = player_img.width/9

    max_word_amt = 5
    focused_word_idx = -1

    speed = 1
    default_speed = 1
    speed_incr = 1
    speed_decr = .4
    speed_time = 120 #frames, 2s
    speed_timer = 0

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

    diff_btn_img.draw(easy_btn_x,diff_btn_y)
    engine.draw_text("EASY", easy_btn_x+diff_btn_width/2, diff_btn_y+btn_height/2,True)

    diff_btn_img.draw(medium_btn_x,diff_btn_y)
    engine.draw_text("MEDIUM",medium_btn_x+diff_btn_width/2,diff_btn_y+btn_height/2,True)

    diff_btn_img.draw(hard_btn_x,diff_btn_y)
    engine.draw_text("HARD",hard_btn_x+diff_btn_width/2,diff_btn_y+btn_height/2,True)

    btn_img.draw(quit_btn_x, quit_btn_y+btn_offset)
    engine.draw_text("QUIT", engine.width/2,engine.height/2+btn_height+btn_offset, True)

    pass

def draw_visuals():
    """
    draws the visuals (background and player)
    :return:
    """
    global player_img, player_sprite_width, speed

    engine.background_color = (0.5607843137254902, 0.8235294117647058, 0.2980392156862745)

    for i in range(len(layers)):  # set every layer's x pos to 0
        list_x_pos.append(0)  # add one at 0
        list_x_pos.append(engine.width)  # add one just off-screen

    for i in range(len(layers)):  # draw every layer
        layers[i].draw(list_x_pos[2 * i], 0)  # 0,2,4...
        layers[i].draw(list_x_pos[2 * i + 1], 0)  # 1,3,5...

    animate_parallax(speed)

    player_img.draw_partial(60,ground_height,(0,0,player_img.height,player_sprite_width))

    pass

def draw_game_text():
    """
    draws words on the screen and colours them as you type
    :return:
    """
    global current_words,displayed_word,typed_letters, displayed_words, focused_word_idx

    engine.set_font_size(20)

    for i, (word, x, y) in enumerate(displayed_words):
        engine.color = 1, 1, 1
        engine.draw_text(word, x, y)

    #draws green over the word
    if focused_word_idx != -1:
        word,x,y = displayed_words[focused_word_idx]
        engine.color = 0, 1, 0
        engine.draw_text(typed_letters, x, y)

    pass

def animate_parallax(speed_multiplier):
    """
    animates the background with parallax effect
    :return:
    """
    global list_x_pos

    dflt_spd = 2

    offset = engine.width

    for i in range(0,len(list_x_pos),2):
        layer_nr = i//2 #0=0,1=0,2=1,3=1,4=2,5=2...

        spd = dflt_spd*(layer_nr+speed_multiplier)
        list_x_pos[i] -= spd
        list_x_pos[i+1] -= spd

        if list_x_pos[i] <= -offset:
            list_x_pos[i] += engine.width*2
        if list_x_pos[i+1] <= -offset:
            list_x_pos[i+1] += engine.width*2

    pass


def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """

    if current_state == GameState.PLAY:
        add_word()
        speed_handler()

    pass

def speed_handler():
    """
    counts down the timer and resets the speed when the timer hits 0.
    :return:
    """
    global speed_timer, speed

    if speed_timer > 0:
        speed_timer -= 1
        if speed_timer == 0:
            speed = default_speed
            print(f"going back to speed: {speed}")

    pass


def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    """
    This function is only executed once each time a mouse button was pressed!
    """
    global current_state
    if current_state == GameState.START:
        if (easy_btn_x < mouse_x < easy_btn_x+diff_btn_width) and (diff_btn_y<mouse_y<diff_btn_y+btn_height):
            print("easy chosen")
            pick_difficulty(1)
            current_state = GameState.PLAY
        elif (medium_btn_x < mouse_x < medium_btn_x+diff_btn_width) and (diff_btn_y<mouse_y<diff_btn_y+btn_height):
            print("medium chosen")
            pick_difficulty(2)
            current_state = GameState.PLAY
        elif (hard_btn_x < mouse_x < hard_btn_x+diff_btn_width) and (diff_btn_y<mouse_y<diff_btn_y+btn_height):
            print("hard chosen")
            pick_difficulty(3)
            current_state = GameState.PLAY
        elif (quit_btn_x < mouse_x < quit_btn_x+btn_width) and (quit_btn_y+btn_offset < mouse_y < quit_btn_y+btn_height+btn_offset):
            quit()

    pass

def pick_difficulty(idx:int):
    match idx:
        case 1:
            current_words.clear()
            current_words.extend(easy_words)
        case 2:
            current_words.clear()
            current_words.extend(medium_words)
        case 3:
            current_words.clear()
            current_words.extend(hard_words)
    pass



def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    global current_state
    if current_state == GameState.PLAY:
        if key == "ESCAPE":
            current_state = GameState.START
        elif key.isalpha():
            spell_checker(key)
        #elif key == " ":
        #    add_word()

    print(f"score: {score}, mistakes: {mistakes}")

    pass

def spell_checker(k):
    """
    checks if the typed letter is the same as the next letter in the displayed word.
    :param k: pressed key
    :return:
    """
    global current_words, displayed_word, displayed_words, focused_word_idx, typed_letters, mistakes, speed

    if focused_word_idx == -1: #no word focused
        for i, (word, x, y) in enumerate(displayed_words):
            if word.startswith(k):
                focused_word_idx = i
                typed_letters = k
                return
        print(f"{k.lower()} - no words start with that (Red)")
        score_handler(-1)
        return

    # Check the focused word
    word, x, y = displayed_words[focused_word_idx]
    if k == word[len(typed_letters)]:
        print(f"{k.lower()} - 👍 (Green)")
        typed_letters += k
        if word == typed_letters: #if word complete
            print(f"{word} - correct spelling (Green)")
            displayed_words.pop(focused_word_idx)
            focused_word_idx = -1
            score_handler(1)
            typed_letters = ""
            if len(displayed_words) == 0:
                add_word()
    else:
        for i, (new_word, x, y) in enumerate(displayed_words):
            if i != focused_word_idx and new_word.startswith(typed_letters + k):
                print(f"{k} - switching word")
                focused_word_idx = i
                typed_letters += k
                return
        print(f"{k.lower()} - wrong, try again (Red)")
        score_handler(-1)

    pass

def score_handler(points:int):
    """
    calculates the score by checking is the word is correct or not.
    :param points:
    :return:
    """
    global score, mistakes, speed, speed_timer

    score += points

    if points >= 0:
        speed += speed_incr
        speed_timer = speed_time #start speeding
        print(f"speed: {speed}, timer: {speed_timer} ")
    if points < 0:
        mistakes -= points
        if not speed >= speed_decr:
            speed -= speed_decr
        speed_timer = speed_time #start slowing
        print(f"speed: {speed}, timer: {speed_timer} ")

    pass

def next_word():
    """
    resets typed letters and picks a new word to display
    :return:
    """
    global current_words, displayed_word, typed_letters

    typed_letters = ""
    displayed_word = random.choice(current_words)

    pass

def add_word():
    """
    adds a new word on the screen in a random position. Only if there is fewer words than the maximum words allowed
    :return:
    """
    global displayed_words, current_words, max_word_amt

    if len(displayed_words) < max_word_amt:
        word = random.choice(current_words)
        x = random.randint(engine.width // 2, engine.width - 50)
        y = random.randint(50, engine.height - 50)
        displayed_words.append((word, x, y))


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
