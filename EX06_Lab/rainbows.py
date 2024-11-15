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


# TODO 3: Ask the user for a sentence they want to 'rainbownize'
#   Print every character with background color black and a random bright foreground color