
def char_appears(sentence, char):
    return [word.lower().count(char) for word in sentence.split()]

