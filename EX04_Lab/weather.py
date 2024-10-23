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

def wind_conditions(strength: int):
    calm_wind = 0, 5, "calm", "No wind, or barely noticeable. Smoke rises straight up, leaves are still"
    breeze_wind = 5, 28, "breeze", "Light to moderate breeze. Leaves rustle, small branches move, flags flutter."
    strong_breeze_wind = 29, 49, "strong breeze", "Large branches sway, dust and paper blow around. Difficult to use an umbrella."
    gale = 50, 74, "gale", "Trees in motion, walking against the wind is hard. Minor structural damage possible."
    storm = 74, "storm", "Severe winds, tree branches break, roofs and buildings may suffer damage. Dangerous."

    if strength < 0:
        print("undefined".upper())
        print("---------")
        input("Wind: ")
    pass

print("[You] Mom, what should I wear?")
print("[Mom] What's the weather like?")
print('("rainy", "sunny", "cold", "snowy", "windy")')
current_weather = input("[You] It's ")
if current_weather in conditions:
    print(f"Oh, then you should wear {what_to_wear(current_weather)}")
else:
    print("Well.. I have no idea, honey.")