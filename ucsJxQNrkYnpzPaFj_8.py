
def char_appears(words,char):
    return [word.lower().count(char) for word in words.split()]

