
def same_length(txt):
    while '10' in txt:
        txt = txt.replace('10', '')
    return len(txt) == 0

