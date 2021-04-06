
def unrepeated(txt):
    word = ""
    for char in txt:
        if char not in word:
            word += char
    return word

