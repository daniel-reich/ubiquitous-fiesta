
def replace_the(txt):
    txt, c = txt.split(" "), 0
    for a in txt:
        if a == "the":
            if txt[c + 1][0] in ["a","e","i","o","u"]: txt[c] = "an"
            else: txt[c] = "a"
        c += 1
    return " ".join(txt)

