
def silence_Trump(txt):
    new = ""
    for ch in txt:
        if ch.lower() not in ['a', 'e', 'i', 'o', 'u']:
            new += ch
    return new

