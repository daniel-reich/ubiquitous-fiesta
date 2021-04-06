
def is_isogram(txt):
    word = txt.lower()
    for i in word:
        if word.count(i) > 1:
            return False
    return True

