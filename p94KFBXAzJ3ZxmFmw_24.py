
def ascii_capitalize(txt):
    output = ""
    for t in txt:
        if((ord(t) % 2) == 0):
            output += t.upper()
        else:
            output += t.lower()
    return output

