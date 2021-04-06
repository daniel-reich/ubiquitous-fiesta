
def silence_Trump(txt):
    string = ""
    vowel = "aeiou"
    for elem in txt:
        if elem.lower() not in vowel:
            string += elem
    return string

