
def neutralise(s1, s2):
    phrase = ""
    for i in list(zip(s1,s2)):
        if i[0] == i[1]:
            if i[0] == "-":
                phrase += "-"
            else:
                phrase += "+"
        else:
            phrase += "0"
    return phrase

