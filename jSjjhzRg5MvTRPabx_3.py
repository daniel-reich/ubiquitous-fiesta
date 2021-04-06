
def sentence(words):
    s = ""
    len_w_1 = len(words) - 1
    for i, w in enumerate(words):
        if i == 0:
            s += "A{} ".format("n" if w[0] in "aeiou" else "") + w + ", "
        elif i == len_w_1:
            s = s[:-2]
            s += " and a{} ".format("n" if w[0] in "aeiou" else "") + w + "."
        else:
            s += "a{} ".format("n" if w[0] in "aeiou" else "") + w + ", "
    return s

