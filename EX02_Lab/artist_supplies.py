import random
art_supplies = "pencil","paint","paintbrush","eraser","sketch paper"

print(len(art_supplies))
print(random.choice(art_supplies))
print(art_supplies[0])
print(art_supplies[-1])

def pick_an_item():
    """
    asks user to pick an index, then shows what variable and type that index holds
    :return:
    """
    more_art_supplies = "reference",True,95,5.4,("orange","blue")
    idx = int(input("pick a number between 0 and 4: "))
    var_type = str(type(more_art_supplies[idx])).split("'")[1]
    print(f"idx {idx} is {more_art_supplies[idx]}, and that is a {var_type}")
    pass

pick_an_item()