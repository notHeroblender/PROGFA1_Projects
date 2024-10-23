last_name = str(input("What is your last name? "))
first_name = str(input("What is your first name? "))
group = int(input("What is your group number? "))
lab_nr = int(input("Which lab is this? "))

print(f"1DAE{group:02d}_{last_name}_{first_name}_L{lab_nr:02d}")