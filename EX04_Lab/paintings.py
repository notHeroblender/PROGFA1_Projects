
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

def is_vip_painter(name: str)-> bool:
    """
    checks if given name is a VIP painter
    :param name:
    :return:
    """
    vip_painters = ("Vincent", "Pablo", "Leonardo", "Claude", "Rembrandt", "Michelangelo", "James")

    if name in vip_painters:
        return True
    else:
        return False
    pass

def ready_to_paint()->bool:
    """
    Asks if user is ready to paint
    :return: answer of user
    """
    answer = input("Are you ready to pant? (yes/no) ")
    answer = answer.lower()
    if (answer == "yes") or (answer == "y") or (answer == "yes!"):
        return True
    else:
        return False

def whats_my_color(r:int,g:int,b:int)->str:
    if r == 1 and g == 0 and b == 0:
        return "red"
    if r == 0 and g == 1 and b == 0:
        return "green"
    if r == 0 and g == 0 and b == 1:
        return "blue"
    if r == 1 and g == 1 and b == 1:
        return "white"
    if r == 0 and g == 0 and b == 0:
        return "black"
    else:
        return "??"

print_title("is_vip_painter", "=")
input_name = input("Welcome, what's your name? ")
if is_vip_painter(input_name):
    print("Welcome, VIP artist! Your canvas awaits!")
else:
    print("Hello, artist! Let's get started with your masterpiece!")

print_title("ready_to_paint", "=")
print(f"This artist is ready to paint: {ready_to_paint()}")

print_title("whats_my_color", "=")
print(f"If r, g, and b are all 0, the colour is {whats_my_color(0,0,0)}.")

red = int(input("r [0-1]: "))
green = int(input("g [0-1]: "))
blue = int(input("b [0-1]: "))

print(f"-> You created the colour {whats_my_color(red, green, blue)}")