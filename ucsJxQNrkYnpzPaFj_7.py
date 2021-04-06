
def char_appears(sentence, char):
    return [i.lower().count(char.lower()) for i in sentence.split()]

