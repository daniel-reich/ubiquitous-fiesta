
def changeTypes(lst):
    new = []
    for i in lst:
        if isinstance(i, int) and i % 2 == 0:
            i = i+1
            new.append(i)
        elif isinstance(i, str):
            i = i.capitalize()
            new.append(i +"!")
        elif isinstance(i, bool):
            i = not bool
            new.append(i)
        else:
            new.append(i)
    return new

