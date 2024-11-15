"""
By using ANSI color codes while printing to the console, you can change the color.
See demo week 03.
This is given start code for the rainbow exercise.
"""
import random


def get_ansi_color_code(color_code: int = 0) -> str:
    """
    Builds the ANSI string that can be used to print console text in a different color.
    :param color_code: Number of the color.
    Foreground, not bright: 30->37. Foreground, bright: 90->97.
    Background, not bright: 40->47. Background, bright: 100->107.
    Use color_code 0 to reset.
    :return: Returns the ANSI string to set the color based on the chosen color code.
    """
    return f"\033[{color_code}m"


# GIVEN START CODE: apply ansi colors to text
color = get_ansi_color_code(93)    # results in bright yellow: \033[93m
reset = get_ansi_color_code(0)     # results in ansi code to reset color: \033[0m
print(f"{color}Test 123!{reset}")  # by printing text in between these ansi color codes, our text appears in a color

fg_black = get_ansi_color_code(30)
fg_gray = get_ansi_color_code(90)
fg_red = get_ansi_color_code(31)
fg_red_bright = get_ansi_color_code(91)
fg_yellow = get_ansi_color_code(33)
fg_yellow_bright = get_ansi_color_code(93)
fg_green = get_ansi_color_code(32)
fg_green_bright = get_ansi_color_code(92)
fg_teal = get_ansi_color_code(36)
fg_teal_bright = get_ansi_color_code(96)
fg_blue = get_ansi_color_code(34)
fg_blue_bright = get_ansi_color_code(94)
fg_purple = get_ansi_color_code(35)
fg_purple_bright = get_ansi_color_code(95)
fg_colours = (fg_black,fg_gray,fg_red,fg_red_bright,fg_yellow,fg_yellow_bright,fg_green,
              fg_green_bright,fg_teal,fg_teal_bright,fg_blue,fg_blue_bright,fg_purple,fg_purple_bright)

bg_black = get_ansi_color_code(40)
bg_gray = get_ansi_color_code(100)
bg_red = get_ansi_color_code(41)
bg_red_bright = get_ansi_color_code(101)
bg_yellow = get_ansi_color_code(43)
bg_yellow_bright = get_ansi_color_code(103)
bg_green = get_ansi_color_code(42)
bg_green_bright = get_ansi_color_code(102)
bg_teal = get_ansi_color_code(46)
bg_teal_bright = get_ansi_color_code(106)
bg_blue = get_ansi_color_code(44)
bg_blue_bright = get_ansi_color_code(104)
bg_purple = get_ansi_color_code(45)
bg_purple_bright = get_ansi_color_code(105)
bg_colours = (bg_black,bg_gray,bg_red,bg_red_bright,bg_yellow,bg_yellow_bright,bg_green,
              bg_green_bright,bg_teal,bg_teal_bright,bg_blue,bg_blue_bright,bg_purple,bg_purple_bright)

# TODO 1: Ask the user for a color code. Show the text "Hello world!" in this color.
#   USE A LOOP: Keep asking until the user entered a correct ansi color number:
#       -> numeric value!
#       -> any numeric value between 30-37 (inclusive) or 90-97 (inclusive) - these are valid foreground colors
#   Only once the user input is correct, use the given get_ansi_color_code to show "Hello world" in the chosen color


inpt = input("Pick ANSI colour code (30-36, 90-96, 40-46, 100-106): ")
while type(inpt) is not int:
    try:
        intinpt = int(inpt)

        if (30 <= intinpt <= 36) or (40 <= intinpt <= 46) or (90 <= intinpt <= 96) or (100 <= intinpt <= 106):
            print(f"{get_ansi_color_code(intinpt)}Hello World!{reset}")
            break
        else:
            print(f"Error: {inpt} not in range of ANSI codes")
            inpt = input("Pick ANSI colour code (30-36, 90-96, 40-46, 100-106): ")
    except ValueError:
        print(f"Error: {inpt} is not an int")
        inpt = input("Pick ANSI colour code (30-36, 90-96, 40-46, 100-106): ")

print("Thanks")

# TODO 2: Print all possible foreground colors and all possible background colors in a table (see screenshots)

print(f"FOREGROUND: \n-----------")
print(f"{fg_black}NORMAL: {30} - {fg_gray}BRIGHT: {90}{reset}")
print(f"{fg_red}NORMAL: {31} - {fg_red_bright}BRIGHT: {91}{reset}")
print(f"{fg_yellow}NORMAL: {33} - {fg_yellow_bright}BRIGHT: {93}{reset}")
print(f"{fg_green}NORMAL: {32} - {fg_green_bright}BRIGHT: {92}{reset}")
print(f"{fg_teal}NORMAL: {36} - {fg_teal_bright}BRIGHT: {96}{reset}")
print(f"{fg_blue}NORMAL: {34} - {fg_blue_bright}BRIGHT: {94}{reset}")
print(f"{fg_purple}NORMAL: {35} - {fg_purple_bright}BRIGHT: {95}{reset}")

print(f"BACKGROUND: \n-----------")
print(f"{get_ansi_color_code(40)}NORMAL: {40} - {get_ansi_color_code(100)}BRIGHT: {100}{reset}")
print(f"{get_ansi_color_code(41)}NORMAL: {41} - {get_ansi_color_code(101)}BRIGHT: {101}{reset}")
print(f"{get_ansi_color_code(43)}NORMAL: {43} - {get_ansi_color_code(103)}BRIGHT: {403}{reset}")
print(f"{get_ansi_color_code(42)}NORMAL: {42} - {get_ansi_color_code(102)}BRIGHT: {102}{reset}")
print(f"{get_ansi_color_code(46)}NORMAL: {46} - {get_ansi_color_code(106)}BRIGHT: {106}{reset}")
print(f"{get_ansi_color_code(44)}NORMAL: {44} - {get_ansi_color_code(104)}BRIGHT: {104}{reset}")
print(f"{get_ansi_color_code(45)}NORMAL: {45} - {get_ansi_color_code(105)}BRIGHT: {105}{reset}")

# TODO 3: Ask the user for a sentence they want to 'rainbowize'
#   Print every character with background color black and a random bright foreground color

text = input("sentence: ")
for ltr in text:
    print(f"{random.choice(fg_colours)}{ltr}{reset}",end="")