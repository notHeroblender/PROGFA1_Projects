import random

names = ("Blinky", "Zap", "Wiggles", "Snoop", "Fizz", "Buzz", "Nibs", "Flip", "Zonk", "Loop", "Chomp")
messages = ("Welcome aboard,", "Oh no, here comes", "Look who decided to join us:", "Say hi to", "Well helloooo",
            "Yikes, they're here:", "Beware! Here's", "Looking good,", "Late to the party,", "Join the club,")

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
reset = get_ansi_color_code(0)

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

for name in names:
    clr = random.choice(fg_colours)
    msg = random.choice(messages)
    print(f"{msg} {clr}{name}!{reset}")