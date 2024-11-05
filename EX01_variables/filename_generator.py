def clean_string(toclean:str)->str:
    """
    cleans off spaces, inner spaces and dashes replaced with underscore, apostrophes deleted
    :return:
    """
    toclean.strip()
    if course == 0:
        toclean = toclean.replace(" ", "_")
        toclean = toclean.replace("-", "_")
    elif course == 1:
        toclean = toclean.replace(" ", "")
        toclean = toclean.replace("-", "")
    toclean = toclean.replace("'","")

    return toclean

def course_selection():
    if course == 0:
        print(f"1DAE{group:02d}_{clean_string(last_name)}_{clean_string(first_name)}_L{lab_nr:02d}")
    elif course == 1:
        print(f"{clean_string(last_name)}_{clean_string(first_name)}_1DAE{group:02d}_{lab_nr:02d}")

last_name = str(input("What is your last name? "))
first_name = str(input("What is your first name? "))
group = int(input("What is your group number? "))
lab_nr = int(input("Which lab is this? "))
print("[0] Programming for Artists")
print("[1] Preproduction")
course = int(input("What course is this for? "))
course_selection()