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