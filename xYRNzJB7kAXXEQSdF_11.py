
def wiggle_string(s):
    lst = []
    lst.append(s)
    for l in range(1, 2 * len(s) + 1):
        if l < len(s):
            lst.append(l * ' ' + s)
        else:
            lst.append((2 * len(s) - l) * ' ' + s)
    return lst

