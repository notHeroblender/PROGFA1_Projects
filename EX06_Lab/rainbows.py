"""
By using ANSI color codes while printing to the console, you can change the color.
See demo week 03.
This is given start code for the rainbow exercise.
"""


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

fg_black = 30
fg_gray = 90
fg_red = 31
fg_red_bright = 91
fg_yellow = 33
fg_yellow_bright = 93
fg_green = 32
fg_green_bright = 92
fg_teal = 36
fg_teal_bright = 96
fg_blue = 34
fg_blue_bright = 94
fg_purple = 35
fg_purple_bright = 95

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
print(f"{get_ansi_color_code(fg_black)}NORMAL: {fg_black} - {get_ansi_color_code(fg_gray)}BRIGHT: {fg_gray}{reset}")
print(f"{get_ansi_color_code(fg_red)}NORMAL: {fg_red} - {get_ansi_color_code(fg_red_bright)}BRIGHT: {fg_red_bright}{reset}")
print(f"{get_ansi_color_code(fg_yellow)}NORMAL: {fg_yellow} - {get_ansi_color_code(fg_yellow_bright)}BRIGHT: {fg_yellow_bright}{reset}")
print(f"{get_ansi_color_code(fg_green)}NORMAL: {fg_green} - {get_ansi_color_code(fg_green_bright)}BRIGHT: {fg_green_bright}{reset}")
print(f"{get_ansi_color_code(fg_teal)}NORMAL: {fg_teal} - {get_ansi_color_code(fg_teal_bright)}BRIGHT: {fg_teal_bright}{reset}")
print(f"{get_ansi_color_code(fg_blue)}NORMAL: {fg_blue} - {get_ansi_color_code(fg_blue_bright)}BRIGHT: {fg_blue_bright}{reset}")
print(f"{get_ansi_color_code(fg_purple)}NORMAL: {fg_purple} - {get_ansi_color_code(fg_purple_bright)}BRIGHT: {fg_purple_bright}{reset}")

print(f"BACKGROUND: \n-----------")
print(f"{get_ansi_color_code(40)}NORMAL: {40} - {get_ansi_color_code(100)}BRIGHT: {100}{reset}")
print(f"{get_ansi_color_code(41)}NORMAL: {41} - {get_ansi_color_code(101)}BRIGHT: {101}{reset}")
print(f"{get_ansi_color_code(43)}NORMAL: {43} - {get_ansi_color_code(103)}BRIGHT: {403}{reset}")
print(f"{get_ansi_color_code(42)}NORMAL: {42} - {get_ansi_color_code(102)}BRIGHT: {102}{reset}")
print(f"{get_ansi_color_code(46)}NORMAL: {46} - {get_ansi_color_code(106)}BRIGHT: {106}{reset}")
print(f"{get_ansi_color_code(44)}NORMAL: {44} - {get_ansi_color_code(104)}BRIGHT: {104}{reset}")
print(f"{get_ansi_color_code(45)}NORMAL: {45} - {get_ansi_color_code(105)}BRIGHT: {105}{reset}")

# TODO 3: Ask the user for a sentence they want to 'rainbownize'
#   Print every character with background color black and a random bright foreground color