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
    picks random item from given tuple.
    :param to_chose_from: tuple holding all presents
    :return: one of the presents
    """
    return random.choice(to_chose_from)

print_title("let Oprah decide","=")
present = oprah_picks(possible_presents)
print(f"And you get a {present}, and you get a {present}, and you get a {present}!")
present = oprah_picks(possible_presents)
print(f"And you get a {present}, and you get a {present}, and you get a {present}!")


def calculate_change(price:float, paid_amount:float)->tuple:
    """
    calculates the change.
    :param price: amount the item costs
    :param paid_amount: amount the customer pays
    :return: a tuple which holds price,paid amount and the change
    """
    result = paid_amount-price
    return price,paid_amount,result

print_title("What's my change?","=")
total,paid,change = calculate_change(123,150)
print(f"If an item costs ${total} and the customer pays ${paid}, their change is ${change}")
total = float(input("[TOTAL] EUR "))
paid = float(input("[PAID]  EUR "))
_,_,change = calculate_change(total,paid)
print("[CHANGE] EUR ",change)


def rgb_to_engine(r:int,g:int,b:int)->tuple:
    """
    calculates colour values out of 255 to values out of 1
    :param r: red value
    :param g: green value
    :param b: blue value
    :return: a tuple with rgb values
    """
    return r/255,g/255,b/255

print_title("Engine colours","=")
print(f"{rgb_to_engine(0,255,125)}")
red = int(input("R: "))
green = int(input("G: "))
blue = int(input("B: "))
print(f"({rgb_to_engine(red,green,blue)})")