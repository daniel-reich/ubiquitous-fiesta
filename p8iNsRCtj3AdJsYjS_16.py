
def title_to_number(s):
    ltrs = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return sum(ltrs.index(s[len(s)-i-1]) * 26**i for i in range(len(s)))

