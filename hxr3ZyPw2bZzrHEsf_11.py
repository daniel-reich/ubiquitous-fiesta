
def make_title(txt):
    l = []
    for i in txt.split():
        if i[0].isupper() is False:
            i = i[0].upper() + i[1:]
        l.append(i)
    return " ".join(l)

