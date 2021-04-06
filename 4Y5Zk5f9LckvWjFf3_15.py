
def special_reverse(x, y):
    s = ''
    for each in x.split():
        if each.startswith(y):
            s += each[::-1] + " "
        else:
            s += each + " "
    return s[:-1]

