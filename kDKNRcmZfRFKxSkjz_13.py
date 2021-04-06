
def unmix(txt):
    new_string = ""
    if len(txt) % 2 == 0:
        for i in range(0, len(txt), 2):
            new_string = new_string + txt[i+1]
            new_string = new_string + txt[i]
    else:
        for i in range(0, len(txt)-1, 2):
            new_string = new_string + txt[i+1]
            new_string = new_string + txt[i]
        new_string = new_string + txt[len(txt) - 1]
    return new_string

