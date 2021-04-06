
def remove_special_characters(txt):
    word = ""
    for i in txt:
        if i.isalpha() or i.isnumeric() or i in " -_":
            word += i
    return word

