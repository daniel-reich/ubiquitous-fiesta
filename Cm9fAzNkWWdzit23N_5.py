
def wave(txt):
    return [txt[:i] + txt[i:].capitalize() for i in range(len(txt)) if txt[i].isalpha()]

