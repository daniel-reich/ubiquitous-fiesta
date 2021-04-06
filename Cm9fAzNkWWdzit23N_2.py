
def wave(txt):
    new = []
    for (i, char) in enumerate(txt):
        if char == ' ':
            continue
        else:
            word = txt[0:i] + char.upper() + txt[i+1:]
            new.append(word)
    return new

