
def invert(s):
    words = list(s)
    words.reverse()
    for i in range(len(words)):
        if words[i].isupper():
            words[i] = words[i].lower()
        elif words[i].islower():
            words[i] = words[i].upper()
    return "".join(words)

