
def is_isogram(txt):
    txt = txt.lower()
    for letter in txt:
        if txt.count(letter) > 1:
            return False
    return True

