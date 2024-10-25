import random
hogwards_houses = ('Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin')
spells = ("Expelliarmus", "Expecto Patronum", "Wingardium Leviosa", "Stupefy", "Accio")

students = (
        ("Harry", "Potter"),
        ("Hermione", "Granger"),
        ("Ron", "Weasley"),
        ("Draco", "Malfoy"),
        ("Neville", "Longbottom"),
        ("Luna", "Lovegood"),
        ("Ginny", "Weasley"),
        ("Fred", "Weasley"),
        ("George", "Weasley"),
        ("Cedric", "Diggory"),
        ("Cho", "Chang"),
        ("Seamus", "Finnigan"),
        ("Dean", "Thomas"),
        ("Lavender", "Brown"),
        ("Pansy", "Parkinson"),
        ("Parvati", "Patil"),
        ("Padma", "Patil")
    )

def assign_house():
    print(f"The Sorting Hat has spoken. Welcome to {random.choice(hogwards_houses)}")
    pass

def random_spell():
    global spells
    print(random.choice(spells))
    pass

def show_frenemy():
    global students
    idx = random.randint(0,15)
    print(f"{students[idx][0]} {students[idx][1]}")
    pass

assign_house()
random_spell()
show_frenemy()