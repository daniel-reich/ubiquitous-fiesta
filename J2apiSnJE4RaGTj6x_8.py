
def find_broken_keys(txt1, txt2):
    nl = []
    for a, b in zip(txt1, txt2):
        if a != b and a not in nl:
            nl.append(a)
    return nl

