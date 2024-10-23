name_l = str(input("The person sitting to my left is called "))
country_l = str(input(f"{name_l} is from "))
age_l = int(input(f"The age of {name_l} from {country_l} is "))

name_r = str(input("The person sitting to my left is called "))
country_r = str(input(f"{name_r} is from "))
age_r = int(input(f"The age of {name_r} from {country_r} is "))

print(f"The average age of {name_l} and {name_r} is {(age_l+age_r)/2}")