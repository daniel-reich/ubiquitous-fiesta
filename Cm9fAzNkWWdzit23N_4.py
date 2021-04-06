
def wave(txt):
    result = []
    for i, c in enumerate(txt):
        if c == ' ':
            continue
        else:
            word = txt[0:i] + c.upper() + txt[i+1:]
            result.append(word)
    return result

