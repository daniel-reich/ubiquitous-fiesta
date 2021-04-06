
def tweak_letters(txt, lst):
    r = ""
    for x, y in zip(txt, lst):
        if x == "z" and y == 1:
            r += "a"
        elif x == "a" and y == -1:
            r += "z"
        elif y == 0:
            r += x
        else:
            r += chr(ord(x) + y)
    return r

