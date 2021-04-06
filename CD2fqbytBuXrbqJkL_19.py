
def can_build(txt1, txt2):
    txt1 = txt1.replace(" ", "")
    txt2 = list(txt2.replace(" ", ""))
    for ch in txt1:
        if ch in txt2:
            txt2.remove(ch)
        else:
            return False
    return True

