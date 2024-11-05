from random import randint

conditions = ("rainy", "sunny", "cold", "snowy", "windy")
outfits = ("raincoat", "sun hat", "sweater", "scarf and gloves", "beanie")

def what_to_wear(weather: str)->str:
    """
    takes a type of weather as input and matches it with another tuple,
    returning fitting clothing for that weather
    :param weather:
    :return:
    """
    global conditions
    global outfits

    idx = conditions.index(weather)
    return outfits[idx]


print("[You] Mom, what should I wear?")
print("[Mom] What's the weather like?")
print('("rainy", "sunny", "cold", "snowy", "windy")')
current_weather = input("[You] It's ")
if current_weather in conditions:
    print(f"Oh, then you should wear {what_to_wear(current_weather)}")
else:
    print("Well.. I have no idea, honey.")


def wind_conditions(strength: int):
    """
    tells you what the wind is like (i think i did it wrong. i didn't use tuple.index())
    :param strength: int value how strong the wind is
    :return:
    """
    calm_wind = 5, "calm", "No wind, or barely noticeable. Smoke rises straight up, leaves are still"
    breeze_wind = 28, "breeze", "Light to moderate breeze. Leaves rustle, small branches move, flags flutter."
    strong_breeze_wind = 49, "strong breeze", "Large branches sway, dust and paper blow around. Difficult to use an umbrella."
    gale = 74, "gale", "Trees in motion, walking against the wind is hard. Minor structural damage possible."
    storm = 74, "storm", "Severe winds, tree branches break, roofs and buildings may suffer damage. Dangerous."

    if strength < 0:
        print("undefined".upper())
        print("---------")
        print("Wind:", strength, "km/h")
        print("Invalid")
        print()
    elif strength <= calm_wind[0]:
        print(calm_wind[1].upper())
        print("-" * len(calm_wind[1]))
        print("Wind:", strength, "km/h")
        print(calm_wind[2])
        print()
    elif strength <= breeze_wind[0]:
        print(breeze_wind[1].upper())
        print("-" * len(breeze_wind[1]))
        print("Wind:", strength, "km/h")
        print(breeze_wind[2])
        print()
    elif strength <= strong_breeze_wind[0]:
        print(strong_breeze_wind[1].upper())
        print("-" * len(strong_breeze_wind[1]))
        print("Wind:", strength, "km/h")
        print(strong_breeze_wind[2])
        print()
    elif strength <= gale[0]:
        print(gale[1].upper())
        print("-" * len(gale[1]))
        print("Wind:", strength, "km/h")
        print(gale[2])
        print()
    else:
        print(storm[1].upper())
        print("-" * len(storm[1]))
        print("Wind:", strength, "km/h")
        print(storm[2])
        print()
    pass

wind_conditions(-4)
wind_conditions(randint(0,100))
wind_conditions(int(input("How strong is the wind? ")))

