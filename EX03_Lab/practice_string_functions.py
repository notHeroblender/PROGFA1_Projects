def proper_caps(txt):
    words = txt.split()
    caps_words = ""
    for word in words:
        if (word.lower() == "of") or (word.lower() == "the"):
            caps_words += " " + word.lower()
        else:
            caps_word = word[0].upper() + word[1:].lower()
            caps_words += " " + caps_word
    return caps_words.strip()
    pass

inpt = input("Enter a movie name: ")
print(f"* WATCH NOW * {proper_caps(inpt)}")


def hide_vowels(text):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        text = text.replace(vowel, "*")
    return text

inpt = input("Enter a word to guess: ")
print("* This word is secret:",hide_vowels(inpt))
print(".\n.\n.\n.\n* psst.. don't tell anyone.. the actual word is", inpt)


def hangman(letter:str="")-> tuple:
    """
    lets the user guess a letter in a hidden word
    :param letter: user's guess
    :return: a tuple with 4 values/ 0. the hidden word as a string/ 1. the number of characters the given letter appears in the word/ 2. the first index of the letter in the word/ 3. the last index of the letter in the word
    """
    word = "occurrence"
    hidden = "*" * len(word)

    amount = word.count(letter)
    first = word.find(letter)
    last = word.rfind(letter)

    return hidden,amount,first,last

inpt = input(f"Please enter a single character you want to find in my hidden word {hangman()[0]}: ")
print("* NUMBER OF TIMES THE CHARACTER IS IN THIS WORD:",hangman(inpt)[1])
print("* FIRST INDEX OF THE CHARACTER IN THIS WORD:",hangman(inpt)[2])
print("* LAST INDEX OF THE CHARACTER IN THIS WORD:",hangman(inpt)[3])


def filename_decoder(filename:str):
    first = filename.split("_")[1]
    last = filename.split("_")[2]
    group = filename.split("_")[0]

    return group,first,last

inpt = input("Enter a filename of your project(group_lastname_firstname): ")
print("* FIRST NAME:", filename_decoder(inpt)[2])
print("* LAST NAME:", filename_decoder(inpt)[1])
print("* GROUP:", filename_decoder(inpt)[0])