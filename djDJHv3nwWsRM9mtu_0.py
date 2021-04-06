
def validate_spelling(txt):
    spelling, word = txt.rsplit(' ', 1)
    return spelling[::3] == word[:-1].upper()

