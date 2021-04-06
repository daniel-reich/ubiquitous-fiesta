
def same_letter_pattern(txt1, txt2):
    if len(txt1) != len(txt2):
        return False
    for i in range(len(txt1)-1):
        if (txt1[i] in txt1[i+1:] and txt2[i] not in txt2[i+1:]) or (txt1[i] not in txt1[i+1:] and txt2[i] in txt2[i+1:]) or (txt1[i] in txt1[i+1:] and txt2[i] in txt2[i+1:] and txt1[i+1:].index(txt1[i])!=txt2[i+1:].index(txt2[i])):
            return False
    return True

