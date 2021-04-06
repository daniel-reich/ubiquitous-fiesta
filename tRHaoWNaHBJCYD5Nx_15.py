
def same_letter_pattern(txt1, txt2):
    if len(txt1) != len(txt2):
        return False
    d1 = {}
    for i in range(len(txt1)):
        if txt1[i] not in d1:
            d1[txt1[i]] = txt2[i]
        else:
            if d1[txt1[i]] != txt2[i]:
                return False
    return True

