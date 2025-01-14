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
boost_lines_y = []
boost_lines_x = []
boost_lines_amt = 0 #how many lines
boost_lines_offset = 0 #random added value for x pos
health_bar_height = 30
#Logic
typed_letters = ""
displayed_word = ""
displayed_words = []
max_word_amt = 0
focused_word_idx = 0
current_words = []
easy_words = [
    "cat", "dog", "sun", "moon", "star", "ball", "tree", "book", "fish", "bird", "red", "blue", "green", "run", "jump",
    "play", "happy", "funny", "house", "cake", "milk", "chair", "table", "apple", "banana", "car", "train", "park",
    "sky", "rain", "snow", "sleep", "smile", "friend", "school", "baby", "mom", "dad", "sister", "brother", "garden",
    "window", "family", "music", "summer", "winter", "flower", "animal", "birthday", "holiday", "morning", "night",
    "ocean", "mountain", "river", "teacher", "homework", "chocolate", "cookie", "picnic", "bicycle", "picture",
    "computer", "orange", "purple", "yellow", "circle", "square", "triangle", "market", "doctor", "nurse", "police",
    "firefighter", "pilot", "farmer", "baker", "artist", "dancer", "singer"]
medium_words = [
    "library", "adventure", "history", "science", "nature", "planet", "universe", "energy", "electricity", "dinosaur",
    "volcano", "astronaut", "discovery", "compass", "calendar", "language", "culture", "festival", "explore", "journey",
    "mystery", "question", "answer", "butterfly", "elephant", "kangaroo", "waterfall", "rainbow", "thunder",
    "lightning", "whisper", "shadow", "blanket", "pillow", "kitchen", "restaurant", "hospital", "grocery", "theater",
    "museum", "assemble", "boundary", "calculate", "describe", "equation", "fraction", "generous", "harmony",
    "illustrate", "journal", "knowledge", "village", "measure", "natural", "opposite", "passage", "pattern", "reason",
    "special", "thousand", "biography", "architect", "engineer", "organism", "atmosphere", "circulation", "digestion",
    "skeleton", "microscope", "telescope", "precipitation", "evaporation", "geography", "continent", "government",
    "democracy", "economy", "literature", "expression", "analysis", "algebra", "geometry", "psychology", "philosophy",
    "hypothesis", "experiment", "bacteria", "chromosome", "biodiversity", "equilibrium", "momentum", "velocity",
    "acceleration", "metamorphosis", "circumference", "diameter", "radius", "proportion", "estimate", "conclusion",
    "analysis", "evaluate", "justify", "kinetic", "longitude", "magnitude", "numerator", "organism", "perimeter",
    "quotient", "ratio", "sequence", "thermal", "variable", "wavelength", "xylem", "zoology", "classify", "summarize",
    "interpret"]
hard_words = [
    "civilization", "architecture", "archaeology", "anthropology", "bureaucracy", "constitution", "legislature",
    "judiciary", "economics", "inflation", "recession", "globalization", "innovation", "technology", "communication",
    "satellite", "astronomy", "meteorology", "geology", "genetics", "abnegation", "commensurate", "diffident",
    "egregious", "fastidious", "grandiose", "histrionic", "incongruous", "juxtapose", "kindle", "levity", "myriad",
    "neophyte", "obfuscate", "perfunctory", "quixotic", "recalcitrant", "sanguine", "vexation", "abstemious",
    "antediluvian", "belligerent", "circumlocution", "disingenuous", "esoteric", "fatuous", "grandiloquent", "hubris",
    "impetuous", "juxtaposition", "magnanimous", "nonchalant", "ostentatious", "perfidious", "querulous", "sagacious",
    "tantamount", "vacillate", "wistful", "acquiesce", "bourgeois", "chicanery", "deleterious", "enervate", "facetious",
    "gregarious", "hegemony", "incontrovertible", "jejune", "lugubrious", "obsequious", "pecuniary", "quotidian",
    "recapitulate", "supercilious", "tempestuous", "unctuous", "vacuous", "xenophobe", "quizzical", "xylophone",
    "jubilant", "subtlety", "chrysanthemum", "encyclopedia", "ambiguity", "vortex", "zeppelin", "haphazard", "syzygy",
    "phosphorescent", "labyrinthine", "dichotomy", "ephemeral", "persnickety", "onomatopoeia", "fluorescent",
    "ineffable", "proclivity", "mellifluous", "preposterous", "conundrum", "effervescent", "serendipity",
    "transcendent", "cacophony", "apocryphal", "ethereal", "idiosyncrasy", "zeitgeist", "epiphany", "nefarious",
    "iridescent"
    ]
speed = 0
default_speed = 1
speed_incr = 1 #added when boosting
speed_decr = .4 #removed when slowing (?)
speed_time = 0
speed_timer = 0
score_multiplier = 0
play_time = 10 # game time in seconds
play_timer = 0  #countdown for the game
words_completed = [] #list of all the words completed
total_health_points = 10
current_health_points = 0
dmg_buffer = 30 #half a second

#END
end_img:ProgfaImage

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
    """
    puts the right values in the global variables needed for the start screen
    """
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
    """
    puts the right values in the global variables needed for the end screen
    """
    global end_img
    #TODO:
    end_img = engine.load_image("Resources/emoji.png")
    end_img.resize(engine.width,engine.height,False)

    pass

def init_gameplay():
    """
    puts the right values in the global variables needed for the gameplay
    """
    global player_img, layers, player_sprite_width, current_words, max_word_amt, focused_word_idx, \
        speed, default_speed, speed_incr, speed_decr, speed_time, speed_timer, \
        boost_lines_amt, boost_lines_y, boost_lines_x, boost_lines_offset, \
        play_timer, words_completed, total_health_points, current_health_points

    for i in range(layer_amt):
        layers.append(engine.load_image(f"Resources/{i + 1}.png"))
    for j in range(len(layers)):
        layers[j].resize(engine.width,engine.height,False)

    player_img = engine.load_image("Resources/Run.png")
    player_img.resize(1350, 200,True)
    player_sprite_width = player_img.width/9

    max_word_amt = 5
    focused_word_idx = -1

    speed = default_speed
    speed_time = 60 #frames, 1s
    speed_timer = 0

    play_timer = play_time * 60 # * 60 for frames
    words_completed.clear()

    boost_lines_amt = 5
    for i in range(boost_lines_amt):
        boost_lines_y.append(random.randint(5, engine.height-5))
        boost_lines_x.append(random.randint(int(engine.width/2),engine.width))
    boost_lines_offset = 0

    current_health_points = total_health_points

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
    if current_state == GameState.END:
        draw_end()

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

def draw_end():
    global end_img
    #TODO:
    engine.color = 0,0,0,.5
    engine.draw_rectangle(0,0,engine.width,engine.height)

    end_img.draw(end_img.width / 2 - end_img.width / 2, end_img.height / 2 - end_img.height / 2)
    engine.color = 0,0,0,.1
    engine.draw_rectangle(0, 0, engine.width, engine.height)

    engine.color = 1,1,1
    engine.draw_text(f"you scored {score} points and got {len(words_completed)} words correct",engine.width/2,engine.height/2,True)
    avg_time_per_word = round(play_time/len(words_completed),2)
    engine.draw_text(f"that means you took an average of {avg_time_per_word} seconds per word ",engine.width/2,engine.height/2+20,True)

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

    if speed > default_speed:
        draw_boost_effect()

    player_img.draw_partial(60,ground_height,(0,0,player_img.height,player_sprite_width))

    draw_health_bar()

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

def draw_boost_effect():
    """
    draws speed lines on the screen
    """
    global boost_lines_y, boost_lines_x, boost_lines_offset

    line_length = engine.width/5

    engine.color = 1,1,1
    engine.outline_color = 1,1,1

    for x, y in zip(boost_lines_x,boost_lines_y):
        engine.draw_line(engine.width+x-boost_lines_offset,y,
                         engine.width+x+line_length-boost_lines_offset,y,2)

    pass

def draw_health_bar():
    """
    draws a health bar at the top of the screen
    """
    engine.color = 0,0,0
    engine.draw_rectangle(0,0, engine.width, health_bar_height, None)
    engine.color = 1,0,0
    engine.draw_rectangle(0,0,engine.width * (current_health_points / total_health_points), health_bar_height, None)

    pass


def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    if current_state == GameState.PLAY:
        add_word()
        speed_handler()
        animate_parallax(speed)
        animate_boost_effect()
        game_time()

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

def animate_boost_effect():
    """
    adds to the x pos of every line. when they go off-screen, they get reset with a new x and y value.
    """
    global boost_lines_offset, boost_lines_x, boost_lines_y

    for i in range(len(boost_lines_x)): #loop over
        boost_lines_x[i] -= speed*10
        if boost_lines_x[i] < 0 - engine.width - (engine.width/5): #reset out of bounds lines
            boost_lines_x[i] += engine.width
            boost_lines_y[i] = random.randint(5, engine.height-5)

    pass

def game_time():
    global play_timer

    play_timer -= 1
    check_game_end()
    pass

def check_game_end():
    """
    checks if the game time has ran out and changes the gamestate if necessary.
    """
    global current_state
    #TODO: change condition
    if play_timer <= 0:
        print(f"congratulations, end of the game! score: {score}")
        current_state = GameState.END

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
    """
    adds words to the list of words to use. harder difficulties include easier difficulties.
    """

    match idx:
        case 1:
            current_words.clear()
            current_words.extend(easy_words)
        case 2:
            current_words.clear()
            current_words.extend(easy_words)
            current_words.extend(medium_words)
        case 3:
            current_words.clear()
            current_words.extend(easy_words)
            current_words.extend(medium_words)
            current_words.extend(hard_words)
    pass


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    global current_state

    if key == "ESCAPE":
        current_state = GameState.START

    if current_state == GameState.PLAY:
        if key.isalpha():
            spell_checker(key)
            print(f"score: {score}, mistakes: {mistakes}")
    if current_state == GameState.END:
        print("you can stop typing now, the game is over...")

    pass

def spell_checker(k):
    """
    checks if the typed letter is the same as the next letter in the displayed word.
    :param k: pressed key
    :return:
    """
    global current_words, displayed_word, displayed_words, focused_word_idx, typed_letters, mistakes, speed, words_completed

    if focused_word_idx == -1: #no word focused
        for i, (word, x, y) in enumerate(displayed_words):
            if word.startswith(k):
                focused_word_idx = i
                typed_letters = k
                return
        print(f"{k.lower()} - no words start with that")
        return

    # Check the focused word
    word, x, y = displayed_words[focused_word_idx]
    if k == word[len(typed_letters)]:
        print(f"{k.lower()} - 👍")
        typed_letters += k
        if word == typed_letters: #if word complete
            words_completed.append(typed_letters)
            word_complete()
    else:
        for i, (new_word, x, y) in enumerate(displayed_words):
            if i != focused_word_idx and new_word.startswith(typed_letters + k):
                print(f"{k} - switching word")
                focused_word_idx = i
                typed_letters += k
                return
        print(f"{k.lower()} - wrong, try again")
        score_handler(-1)

    pass

def word_complete():
    global focused_word_idx, typed_letters, displayed_words

    word, x, y = displayed_words[focused_word_idx]

    print(f"{word} - correct spelling")
    displayed_words.pop(focused_word_idx)
    focused_word_idx = -1
    check_word_difficulty()
    score_handler(5)
    typed_letters = ""
    if len(displayed_words) == 0:
        add_word()

    pass

def score_handler(points:int):
    """
    calculates the score by checking is the word is correct or not.
    :param points:
    :return:
    """
    global score, mistakes, speed, speed_timer

    score += points * score_multiplier

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

def check_word_difficulty():
    """
    sets the score multiplier according to the word that was just typed.
    """
    global score_multiplier

    if typed_letters in medium_words:
        score_multiplier = 2
    elif typed_letters in hard_words:
        score_multiplier = 4
    else:
        score_multiplier = 1

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

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
