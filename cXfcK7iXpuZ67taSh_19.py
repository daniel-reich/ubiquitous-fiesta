
def mystery_func(txt):
    a = []
    newString = ""
    for char in txt:
        if char.isdigit() is True:
            a.append(int(char))
        else:
            a.append(char)
    for i in a:
        try:
            if a.index(i) < len(a) and type(a[a.index(i) + 1]) == int:
                add = i * a[a.index(i) + 1]
                newString += str(add)
            else:
                pass
        except:
            pass
    return newString

