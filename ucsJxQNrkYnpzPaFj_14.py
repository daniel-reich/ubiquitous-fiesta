
def char_appears(sentence, char):
    new = sentence.split(" ")
    new2 = [s.lower() for s in new]
    return [n.count(char.lower()) for n in new2]

