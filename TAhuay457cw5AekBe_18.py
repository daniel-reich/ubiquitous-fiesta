
def monkey_talk(txt):
    v = "euioa";
    L = []
    for i in txt.split():
        if i[1] in v:
            L.append("Ook")
        else:
            L.append("eek")
    return " ".join(L).capitalize() + "."

