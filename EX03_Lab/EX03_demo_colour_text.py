import random

#get full username
full_name = input("Enter your full name and let the story begin: ")
#print(full_name)

#isolate firstname
def get_first_name(name: str) ->str:
    """
    takes a full name and returns only the first name
    :param name:
    :return:
    """
    #crashes whenever full name doesn't have exactly 2 words, or any unexpected spaces
    #first, last = name.split(" ",1) #maxsplit:1 fixes if more than 2 words
    #firstname = first

    first = name.split()[0]

    return first
    pass

#add prefix and suffix
def get_magical_name(current_name: str) -> str:
    """
    takes name and generates and returns it with a random pre- and suffix
    :param current_name:
    :return:
    """
    prefixes = ("", "uhhh...", "Grand", "Mysterious", "Archmage", "Elder", "Sorcerer", "Enchanter", "Warlock", "The Impostor")
    suffixes = ("", "i guess", "of the Myst", "the Wise", "the All-Knowing", "of the Eternal Flame", "the Spellbinder", "is Among Us")

    rand_prefix = random.choice(prefixes)
    rand_suffix = random.choice(suffixes)

    magicalname = f"{rand_prefix} {current_name} {rand_suffix}"

    return magicalname
    pass

#do action toward enemy
def print_action_battle(player: str, enemy: str):
    """
    prints random attack from player to enemy
    :param player:
    :param enemy:
    :return:
    """
    actions = ("casts a spell on", "punches", "casts testicular torsion on", "ejects", "smites",
               "flips the bird at", "pulls out a .50cal glock and shoots", "does a 360 one-block jump in front of",
               "does a backwards 2-block jump in front of", "dodges the attack of")
    rand_action = random.choice(actions)

    print(f"{player} {rand_action} {enemy}")

    pass

#colour text
def get_coloured_text(text: str, colour_index: int)-> str:
    """
    colours given text with given colour index -> ansi escape code formatting
    https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
    :param text:
    :return:
    """
    return f"\033[{colour_index}m{text}\033[0m"
    pass


#name generating
first_name = get_first_name(full_name)
magical_name = get_magical_name(first_name)
coloured_magical_name = get_coloured_text(magical_name,33)

print(coloured_magical_name)

#enemy generating
enemy_name = "Fizzling Fluffstorm"
enemy = get_coloured_text(enemy_name,31)
#boss generating
boss_name = enemy_name.replace("Fl", "P")
boss_name = boss_name.replace("F", "S")
boss = get_coloured_text(boss_name, 34)

#battle generating
print_action_battle(coloured_magical_name, enemy)
print_action_battle(enemy, coloured_magical_name)
print_action_battle(coloured_magical_name, boss)
print_action_battle(boss, coloured_magical_name)