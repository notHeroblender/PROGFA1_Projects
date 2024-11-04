last_name = str(input("What is your last name? "))
first_name = str(input("What is your first name? "))
group = int(input("What is your group number? "))
lab_nr = int(input("Which lab is this? "))

def clean_string(toclean:str)->str:
    """
    cleans off spaces, inner spaces and dashes replaced with underscore, apostrophes deleted
    :return:
    """
    toclean.strip()
    toclean = toclean.replace(" ","_")
    toclean = toclean.replace("-","_")
    toclean = toclean.replace("'","")

    return toclean


print(f"1DAE{group:02d}_{clean_string(last_name)}_{clean_string(first_name)}_L{lab_nr:02d}")