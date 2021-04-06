
def unrepeated(txt):
    nl = []
    for letter in txt:
        if letter not in nl:
            nl.append(letter)
    return ''.join(nl)

