import random

def print_title(text: str, symbol: str, amount: int=10):
    """
    generates title based on given text, given symbol, and given amount of symbols
    :param text:
    :param symbol:
    :param amount:
    :return:
    """
    print(f"{symbol*amount} {text} {symbol*amount}")
    pass

def generate_compliment()-> str:
    adjectives = ("artful", "colourful")
    nouns = ("artist", "designer")

    rand_adjective = random.choice(adjectives)
    rand_noun = random.choice(nouns)

    return f"{rand_adjective} {rand_noun}"

print_title("functions: time for a compliment","=")
print(f"Wow, you are one {generate_compliment()}!")
print(f"And did you know your neighbour is a {generate_compliment()}?")


possible_presents = ("luxurious cruise ticket", "smart home speaker", "new car", "backwards 360")
def oprah_picks(to_chose_from: tuple):
    """
    picks random item from given tuple
    :param to_chose_from:
    :return:
    """
    return random.choice(to_chose_from)

print_title("let Oprah decide","=")
present = oprah_picks(possible_presents)
print(f"And you get a {present}, and you get a {present}, and you get a {present}!")
present = oprah_picks(possible_presents)
print(f"And you get a {present}, and you get a {present}, and you get a {present}!")
